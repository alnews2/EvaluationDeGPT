# Tests

## Objectif

Les tests servent en priorité à protéger les comportements importants et à détecter les régressions. La couverture permet de mesurer quelles parties du code sont effectivement exécutées par les tests ; elle sert d'indicateur pour identifier les zones à renforcer, sans viser un pourcentage arbitraire.

## Tests unitaires

Les tests de la calculatrice vérifient la logique des quatre opérations et les principaux cas de saisie et d'erreur.

Lancer tous les tests :

```text
uv run pytest
```

## Couverture de code

La couverture est mesurée avec **coverage.py**, via l'environnement de développement.

Lancer les tests avec mesure de couverture :

```text
uv run coverage run -m pytest
```

Afficher le rapport dans le terminal :

```text
uv run coverage report
```

Générer un rapport HTML détaillé :

```text
uv run coverage html
```

Le rapport HTML est généré dans `htmlcov/` et permet d'identifier les lignes non couvertes.

La couverture est calculée avec la couverture des branches activée et porte sur le package `src/evaluation_de_gpt`.

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

La CI Windows exécute Ruff, les tests avec mesure de couverture et produit un rapport HTML de couverture avant de construire l'exécutable avec PyInstaller.

Le rapport HTML est conservé comme artefact GitHub Actions sous le nom `EvaluationDeGPT-coverage`. L'exécutable Windows reste disponible comme artefact séparé lorsque le build réussit.
