# Architecture

## Objectif

L'architecture est volontairement simple. Le projet est une application desktop Python/PySide6 et doit pouvoir évoluer sans introduire prématurément une architecture lourde.

## Organisation

```text
src/evaluation_de_gpt/
├── __init__.py
├── __main__.py
├── calculator.py
├── history.py
├── history_window.py
└── main.py
```

Les responsabilités commencent à être séparées au fur et à mesure que l'application grandit :

- `calculator.py` : logique de calcul indépendante de l'interface ;
- `history.py` : modèle de l'historique des calculs de la session ;
- `history_window.py` : fenêtre PySide6 d'affichage et d'effacement de l'historique ;
- `main.py` : fenêtre principale et orchestration de l'interface.

À mesure que l'application grandira, les responsabilités pourront être séparées progressivement : `ui/`, `viewmodels/`, `domain/`, `services/`, `infrastructure/` ou `config/` pourront être introduits lorsqu'une responsabilité réelle le justifiera.

## Principes

1. Garder les dépendances entre couches explicites.
2. Éviter de placer de la logique métier dans les widgets lorsque celle-ci peut être testée indépendamment.
3. Préférer une évolution incrémentale à une refonte préventive.
4. Conserver une application exécutable et testable à chaque étape.

## Historique des calculs

L'historique est conservé uniquement pendant la session courante de l'application.

Chaque calcul réussi est enregistré sous la forme :

```text
2 + 3 = 5
```

La fenêtre d'historique est ouverte depuis la fenêtre principale et permet d'effacer l'ensemble des entrées. Aucune persistance sur disque n'est actuellement prévue.

La fenêtre d'historique est une fenêtre outil rattachée à la fenêtre principale. Son coin supérieur droit coïncide avec le coin supérieur gauche de celle-ci, et elle suit ses déplacements. Elle est également fermée automatiquement lorsque la fenêtre principale est fermée.

## Point d'entrée

`evaluation_de_gpt.__main__` est le point d'entrée de l'application :

```text
python -m evaluation_de_gpt
```

Il est également utilisé comme point d'entrée par PyInstaller pour la construction Windows.
