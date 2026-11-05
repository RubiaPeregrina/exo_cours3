# Mini-analyste pandas : arménien classique (HYE)

Répondre aux questions Q1–Q5 sur le corpus arménien (HYE) en écrivant puis en lançant un script pandas, `scripts/analyser.py`.

## Règles
- Utiliser uniquement `uv run`, jamais `pip` directement
- Les chiffres doivent tous provenir du résultat du script. Ils ne sont jamais inventés.
- n'utiliser que les fonction de la skill "pandas tuto"
- tu ne lis pas directement les fichiers du dossier `data/`

## Rôles
- L'agent principal transmet les questions au sous-agent `analyste` et rapporte sa réponse sans la modifier.
- L'agent analyste écrit `scripts/analyser.py`, le lance et répond en 5 lignes.

## Repères
- Données : `data/HYE_train.tsv`, `data/HYE_test_in-domain.tsv`, `data/HYE_test_out-of-domain.tsv`, colonnes `text_form form lemma pos`.
- Tagset : `data/HYE_tagset.txt` (étiquette, tabulation, définition).