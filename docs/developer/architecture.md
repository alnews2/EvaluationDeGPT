# Architecture

## Objectif

L'architecture est volontairement simple. Le projet est une application desktop Python/PySide6 et doit pouvoir évoluer sans introduire prématurément une architecture lourde.

## Organisation

```text
src/evaluation_de_gpt/
├── __init__.py
├── __main__.py
└── main.py
```

La première version reste compacte. `main.py` regroupe actuellement la fenêtre et la logique de calcul nécessaire à la calculatrice.

À mesure que l'application grandira, les responsabilités pourront être séparées progressivement :

- `ui/` : fenêtres, widgets et dialogues PySide6 ;
- `viewmodels/` : état et orchestration entre interface et domaine ;
- `domain/` : règles métier indépendantes de PySide6 ;
- `services/` : cas d'usage et services applicatifs ;
- `infrastructure/` : accès aux fichiers, base de données ou systèmes externes ;
- `config/` : configuration de l'application.

Ces répertoires ne doivent être créés que lorsqu'une responsabilité réelle le justifie.

## Principes

1. Garder les dépendances entre couches explicites.
2. Éviter de placer de la logique métier dans les widgets lorsque celle-ci peut être testée indépendamment.
3. Préférer une évolution incrémentale à une refonte préventive.
4. Conserver une application exécutable et testable à chaque étape.

## Point d'entrée

`evaluation_de_gpt.__main__` est le point d'entrée de l'application :

```text
python -m evaluation_de_gpt
```

Il est également utilisé comme point d'entrée par PyInstaller pour la construction Windows.
