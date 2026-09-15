# Démarrage rapide

## Prérequis

Pour exécuter l'application depuis les sources :

- Windows, Linux ou macOS pour le développement ;
- Python 3.13 ou supérieur ;
- [uv](https://docs.astral.sh/uv/) recommandé pour gérer l'environnement et les dépendances.

Pour utiliser la version Windows distribuée, seul l'exécutable généré par le projet est nécessaire.

## Installer l'environnement de développement

Depuis la racine du dépôt :

```text
uv venv
uv sync --extra dev
```

## Lancer l'application

```text
uv run python -m evaluation_de_gpt
```

La fenêtre de la calculatrice s'ouvre alors directement.

## Vérifier le projet

Tests automatisés :

```text
uv run pytest
```

Contrôle statique :

```text
uv run ruff check .
```

Formatage Ruff :

```text
uv run ruff format .
```

## Construire l'exécutable Windows

La construction officielle est réalisée par GitHub Actions avec PyInstaller. La CI vérifie d'abord le code et les tests, puis génère l'exécutable Windows.

Le point d'entrée PyInstaller est `src/evaluation_de_gpt/__main__.py`. Cette entrée permet de lancer correctement le package et ses imports relatifs.

L'artefact produit par la CI est un exécutable nommé `EvaluationDeGPT.exe`.
