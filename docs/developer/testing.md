# Tests

## Objectif

Les tests servent en priorité à protéger les comportements importants et à détecter les régressions. La couverture doit rester pertinente plutôt que viser un pourcentage arbitraire.

## Tests unitaires

Les tests de la calculatrice vérifient la logique des quatre opérations et les principaux cas de saisie et d'erreur.

Lancer tous les tests :

```text
uv run pytest
```

## Contrôle du code

Ruff est exécuté pour détecter les problèmes de style et certaines erreurs courantes :

```text
uv run ruff check .
```

Le formatage peut être contrôlé sans modifier les fichiers :

```text
uv run ruff format --check .
```

## Validation fonctionnelle

Les tests automatisés ne remplacent pas les vérifications de l'interface. Pour une évolution graphique, effectuer également un contrôle manuel de la fonctionnalité concernée.

Une Pull Request doit indiquer les tests automatisés et les contrôles manuels réellement effectués.

## CI

La CI Windows exécute actuellement Ruff et pytest avant de construire l'exécutable avec PyInstaller. Un artefact Windows est publié lorsque le build réussit.
