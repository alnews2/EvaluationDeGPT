# ADR 0001 — Python + PySide6

- **Statut** : accepté
- **Date** : 2026-09-15

## Contexte

L'application est une application desktop qui doit pouvoir évoluer progressivement tout en restant simple à maintenir.

## Décision

Le projet utilise **Python 3.13+** et **PySide6 / Qt 6** pour l'interface graphique.

## Raisons

- Python est adapté au développement rapide et aux tests ;
- PySide6 fournit une interface desktop native multiplateforme basée sur Qt ;
- ces technologies sont déjà maîtrisées pour le projet ;
- l'ensemble reste suffisamment léger pour l'objectif de l'application.

## Alternatives considérées

D'autres frameworks desktop ou une application web embarquée pourraient être envisagés ultérieurement, mais ils apporteraient une complexité inutile à ce stade.

## Conséquence

La logique métier doit autant que possible rester indépendante de PySide6 afin de préserver la testabilité et de faciliter une éventuelle évolution future de l'interface.
