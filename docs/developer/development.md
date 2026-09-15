# Développement

## Environnement

Le projet cible Python 3.13+. `uv` est l'outil recommandé pour créer l'environnement et installer les dépendances.

```text
uv venv
uv sync --extra dev
```

## Lancer l'application

```text
uv run python -m evaluation_de_gpt
```

## Dépendances principales

- **PySide6** : interface graphique Qt 6 ;
- **pytest** : tests automatisés ;
- **Ruff** : lint et formatage ;
- **PyInstaller** : création de l'exécutable Windows.

Les dépendances de développement restent séparées des dépendances nécessaires à l'exécution de l'application.

## Organisation du travail

Les modifications sont réalisées dans des branches dédiées à partir de `main`. Une Pull Request permet ensuite de revoir les changements, de vérifier la CI et de conserver `main` dans un état validé.

Le détail de ce workflow est décrit dans `CONTRIBUTING.md`.

## Avant une Pull Request

Exécuter au minimum :

```text
uv run pytest
uv run ruff check .
```

Si des fichiers Python ont été modifiés, le formatage peut être vérifié avec :

```text
uv run ruff format --check .
```

La CI reproduit les contrôles nécessaires et construit l'exécutable Windows.
