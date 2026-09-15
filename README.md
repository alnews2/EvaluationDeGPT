# EvaluationDeGPT

Application desktop de démonstration développée en Python + PySide6.

## V0 — Calculatrice

La première version propose une calculatrice de quatre opérations :

- addition ;
- soustraction ;
- multiplication ;
- division ;
- nombres décimaux ;
- changement de signe ;
- effacement et retour arrière ;
- gestion de la division par zéro.

La logique de calcul est séparée de l'interface graphique et couverte par des tests unitaires.

## Développement

Python 3.13 ou supérieur est requis.

Avec `uv` :

```text
uv venv
uv sync --extra dev
uv run python -m evaluation_de_gpt
```

Tests :

```text
uv run pytest
```

Analyse/formatage :

```text
uv run ruff check .
uv run ruff format .
```

## Workflow Git

- `main` contient uniquement les versions validées.
- Les évolutions sont développées dans des branches dédiées.
- Les changements sont proposés via Pull Request avant fusion.
