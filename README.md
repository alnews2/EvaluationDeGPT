# EvaluationDeGPT

Application desktop de démonstration développée en **Python + PySide6**.

## État du projet

La version `0.1.0` fournit une première calculatrice de quatre opérations et constitue la base fonctionnelle du projet. Le projet est développé progressivement, avec validation par Pull Request et CI Windows.

## Fonctionnalités actuelles

La calculatrice propose :

- addition ;
- soustraction ;
- multiplication ;
- division ;
- nombres décimaux ;
- changement de signe ;
- effacement et retour arrière ;
- mémorisation du nombre affiché avec `M` ;
- restitution du nombre mémorisé avec `MR` ;
- gestion de la division par zéro.

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

Le build Windows est automatisé par GitHub Actions. La CI exécute Ruff et pytest, puis génère `EvaluationDeGPT.exe` avec PyInstaller.

L'artefact Windows est disponible dans les résultats de la CI lorsque le build réussit.

## Workflow Git

- `main` contient uniquement les versions validées ;
- les évolutions sont développées dans des branches dédiées ;
- les changements sont proposés via Pull Request avant fusion ;
- la CI participe à la validation ;
- la validation finale et la fusion restent sous le contrôle du propriétaire du dépôt.

Les règles détaillées sont décrites dans [CONTRIBUTING.md](CONTRIBUTING.md).
