# Contribuer au projet

Ce document décrit le mode de contribution retenu pour **EvaluationDeGPT**.

## Principes

Le projet privilégie une évolution progressive et vérifiable :

- `main` contient uniquement des versions validées ;
- chaque évolution significative est préparée dans une branche dédiée ;
- les modifications sont proposées par Pull Request (PR) ;
- la CI doit rester verte avant validation ;
- la fusion dans `main` reste soumise à la validation du propriétaire du dépôt.

## Développer une évolution

1. Partir de `main` à jour.
2. Créer une branche descriptive, par exemple `feature/nom-de-la-fonctionnalite` ou `fix/nom-du-probleme`.
3. Implémenter la modification en conservant une séparation claire entre interface, logique métier et services.
4. Ajouter ou adapter les tests correspondant au comportement modifié.
5. Vérifier localement :

   ```text
   uv run pytest
   uv run ruff check .
   ```

6. Ouvrir une Pull Request vers `main`.
7. Vérifier la CI et effectuer les contrôles fonctionnels nécessaires.
8. Faire valider puis fusionner la PR.

## Pull Requests

Une PR doit expliquer clairement :

- **Objectif** : pourquoi la modification est réalisée ;
- **Modifications** : ce qui a changé ;
- **Choix techniques** : décisions importantes et alternatives écartées ;
- **Validation** : tests automatisés et contrôles manuels réalisés ;
- **Risques** : régressions ou points restant à surveiller.

Pour une évolution importante, la documentation concernée doit être mise à jour dans la même PR.

## Qualité du code

Le projet utilise actuellement :

- Python 3.13+ ;
- PySide6 pour l'interface graphique ;
- pytest pour les tests ;
- Ruff pour le contrôle du code ;
- uv pour la gestion de l'environnement et des dépendances ;
- PyInstaller pour la construction de l'exécutable Windows.

Les tests doivent privilégier les comportements importants et les régressions potentielles plutôt qu'un objectif arbitraire de couverture à 100 %.
