# ADR 0003 — PyInstaller pour la distribution Windows

- **Statut** : accepté
- **Date** : 2026-09-15

## Contexte

L'application doit pouvoir être distribuée sous la forme d'un exécutable Windows sans imposer à l'utilisateur final d'installer Python.

## Décision

Utiliser **PyInstaller** pour produire un exécutable Windows autonome à partir du point d'entrée `src/evaluation_de_gpt/__main__.py`.

## Raisons

- intégration simple avec le projet Python ;
- génération d'un exécutable `onefile` ;
- automatisation facile dans GitHub Actions ;
- solution adaptée au stade actuel du projet.

## Alternatives

D'autres outils de packaging pourront être évalués si les besoins de distribution évoluent, notamment pour l'installation, les mises à jour ou la signature du logiciel.

## Conséquence

Le build Windows fait partie de la CI et doit rester reproductible à partir du dépôt.
