# ADR 0004 — Workflow Git léger avec validation par Pull Request

- **Statut** : accepté
- **Date** : 2026-09-15

## Contexte

Le projet est développé progressivement. Il faut pouvoir expérimenter sans déstabiliser `main`, tout en conservant une validation humaine avant fusion.

## Décision

Utiliser un workflow Git léger :

- `main` contient les versions validées ;
- les évolutions sont développées dans des branches dédiées ;
- chaque évolution est proposée par Pull Request ;
- la CI fournit une première validation automatisée ;
- le propriétaire du dépôt conserve la décision finale de fusion.

## Raisons

Ce fonctionnement apporte une traçabilité suffisante sans la complexité d'un GitFlow complet.

## Conséquence

Le nombre de branches permanentes reste limité. Les branches de fonctionnalité ou de correction peuvent être supprimées après fusion.
