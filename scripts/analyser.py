import pandas as pd

train = pd.read_csv("data/HYE_train.tsv", sep="\t")
test_id = pd.read_csv("data/HYE_test_in-domain.tsv", sep="\t")
test_ood = pd.read_csv("data/HYE_test_out-of-domain.tsv", sep="\t")
tagset = pd.read_csv("data/HYE_tagset.txt", sep="\t", header=None)

print("Q1. Quelles sont les 5 categories (pos) les plus frequentes dans le train ?")
vc_pos = train["pos"].value_counts()
print(vc_pos.head(5))
print("total mots train:", len(train), "| somme value_counts:", vc_pos.sum())
print()

print("Q2. Proportion de formes composees (@ dans pos) et 5 combinaisons les plus frecuentes")
compose = train["pos"].str.contains("@")
print("proportion:", compose.mean(), "soit", int(compose.sum()), "mots sur", len(train))
print(train[compose]["pos"].value_counts().head(5))
print()

print("Q3. Mots du train avec article suffixe (@PRO+Dem en fin de pos) et preposition զ (lemma en ז@)")
art = train["pos"].str.contains(r"@PRO\+Dem$")
prep = train["lemma"].str.contains("^զ@")
print("pos finissant par @PRO+Dem:", int(art.sum()))
print("lemma commençant par锌锌@ :", int(prep.sum()))
print()

print("Q4. Etiquettes du train absentes de HYE_tagset.txt (avec leurs comptes)")
valid = set(tagset[0].str.strip().unique())
labels = train["pos"].unique()
bad = []
for lab in labels:
    if not isinstance(lab, str):
        bad.append(lab)
        continue
    parts = [p for p in lab.strip().split("@") if p != ""]
    if any(p not in valid for p in parts):
        bad.append(lab)
counts = train["pos"].value_counts()
bad_counts = counts[counts.index.isin(bad)]
if len(bad_counts) == 0:
    print("(aucune etiquette hors tagset)")
else:
    print(bad_counts)
print()

print("Q5. Dictionnaire (forme -> pos la plus frequente dans le train) evalue sur les tests")
vc_form_pos = train.value_counts(subset=["form", "pos"]).reset_index(name="n")
vc_form_pos = vc_form_pos.sort_values("n", ascending=False).drop_duplicates("form")
dico = vc_form_pos.rename(columns={"pos": "pred"})[["form", "pred"]]
majority = train["pos"].value_counts().head(1).index[0]
print("tag majoritaire du train (repli pour formes inconnues):", majority)


def score_dictionary(test):
    m = test.merge(dico, on="form", how="left")
    pred = m["pred"].fillna(majority)
    return (pred == m["pos"]).mean()


s_id = score_dictionary(test_id)
s_ood = score_dictionary(test_ood)
print("score test in-domain:", round(float(s_id), 4))
print("score test out-of-domain:", round(float(s_ood), 4))
print("baisse in-domain -> out-of-domain:", round(float(s_id - s_ood), 4),
      "(grec: 0,73 -> 0,51, baisse 0,22)")
