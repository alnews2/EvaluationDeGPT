# ADR 0002 — Structure progressive du projet

- **Statut** : accepté
- **Date** : 2026-09-15

## Contexte

L'application doit pouvoir accueillir de nouvelles fonctionnalités sans imposer dès le départ une architecture complexe.

## Décision

Adopter une séparation progressive des responsabilités : interface, logique métier, services et infrastructure sont séparés lorsqu'une complexité réelle apparaît.

La structure cible prévoit notamment `ui/`, `viewmodels/`, `domain/`, `services/`, `infrastructure/` et `config/`, mais ces répertoires ne sont créés que lorsqu'ils apportent une valeur concrète.

## Raisons

Cette approche évite le sur-engineering tout en fournissant une direction claire pour les futures évolutions.

## Conséquence

La structure actuelle peut rester compacte. Toute extraction de module doit répondre à un besoin identifiable : taille, responsabilité, testabilité ou réutilisation.
