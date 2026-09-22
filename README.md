# EvaluationDeGPT

[![Windows build](https://github.com/alnews2/EvaluationDeGPT/actions/workflows/build-windows.yml/badge.svg)](https://github.com/alnews2/EvaluationDeGPT/actions/workflows/build-windows.yml)
[![Latest release](https://img.shields.io/github/v/release/alnews2/EvaluationDeGPT?display_name=tag)](https://github.com/alnews2/EvaluationDeGPT/releases/latest)
[![Python 3.13+](https://img.shields.io/badge/python-3.13%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Qt 6](https://img.shields.io/badge/Qt-6-green?logo=qt&logoColor=white)](https://www.qt.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Application desktop de démonstration développée en **Python + PySide6**.

## État du projet

La calculatrice reprend la version à quatre opérations et ajoute une fonctionnalité de mémoire de calculatrice.

L'interface affiche en permanence le contenu de la mémoire sous l'écran principal.

Le projet est développé progressivement, avec validation par Pull Request et CI Windows. Le workflow de release valide l'installation, l'analyse du code, les tests et la construction Windows avant toute mise à jour de version ou publication.

## Fonctionnalités

La calculatrice propose :

- addition ;
- soustraction ;
- multiplication ;
- division ;
- nombres décimaux ;
- changement de signe ;
- effacement et retour arrière ;
- mémorisation du nombre affiché avec `M` ;
- restitution du nombre mémorisé avec `MR`, comme une saisie clavier ;
- conservation de la mémoire pendant les opérations et l'effacement de l'affichage ;
- affichage permanent de l'état de la mémoire ;
- affichage de `Mémoire : —` lorsqu'aucune valeur n'est mémorisée ;
- affichage de `Mémoire : <valeur>` lorsqu'une valeur est mémorisée ;
- gestion de la division par zéro ;
- historique des calculs de la session dans une fenêtre dédiée ;
- effacement de l'historique depuis sa fenêtre.

La logique de calcul est séparée de l'interface graphique et couverte par des tests automatisés.

## Documentation

- [Démarrage rapide](docs/user/getting-started.md)
- [Utilisation de la calculatrice](docs/user/calculator.md)
- [Architecture](docs/developer/architecture.md)
- [Guide de développement](docs/developer/development.md)
- [Tests](docs/developer/testing.md)
- [Build Windows](docs/developer/build.md)
- [Contribuer au projet](CONTRIBUTING.md)
- [Décisions d'architecture](docs/decisions/)
- [Changelog](CHANGELOG.md)

## Développement

Python **3.13 ou supérieur** est requis.

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

Analyse du code :

```text
uv run ruff check .
```

Vérification du formatage :

```text
uv run ruff format --check .
```

## Build Windows

Le build Windows est automatisé par GitHub Actions. La CI exécute Ruff, les tests avec mesure de couverture, puis génère `EvaluationDeGPT.exe` avec PyInstaller.

Le rapport HTML de couverture et l'artefact Windows sont disponibles dans les résultats de la CI lorsque le build réussit.

## Workflow Git

- `main` contient uniquement les versions validées ;
- les évolutions sont développées dans des branches dédiées ;
- les changements sont proposés via Pull Request avant fusion ;
- la CI participe à la validation ;
- la validation finale et la fusion restent sous le contrôle du propriétaire du dépôt.

Les règles détaillées sont décrites dans [CONTRIBUTING.md](CONTRIBUTING.md).
