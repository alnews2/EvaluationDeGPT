# Calculatrice

## Fonctionnalités

La version actuelle propose une calculatrice graphique à quatre opérations :

- addition ;
- soustraction ;
- multiplication ;
- division ;
- nombres décimaux ;
- changement de signe ;
- effacement complet ;
- retour arrière ;
- mémorisation du nombre affiché (`M`) ;
- restitution du nombre mémorisé (`MR`) ;
- gestion de la division par zéro.

Les calculs utilisent `Decimal` afin d'éviter les imprécisions usuelles des calculs flottants binaires pour les valeurs décimales saisies par l'utilisateur.

## Utilisation

La saisie se fait avec les boutons de la fenêtre :

- les chiffres permettent de construire le nombre courant ;
- `.` saisit le séparateur décimal ;
- `+`, `-`, `×` et `÷` sélectionnent l'opération ;
- `=` calcule le résultat ;
- `C` efface la saisie et réinitialise l'état de calcul, sans effacer la mémoire ;
- `⌫` supprime le dernier caractère ;
- `±` inverse le signe du nombre courant ;
- `M` mémorise le nombre affiché, sauf si l'affichage indique `Erreur` ;
- `MR` restitue le nombre mémorisé comme une saisie clavier : il remplace l'affichage lorsqu'un nouvel opérande est attendu et s'ajoute à la saisie courante dans les autres cas.

La mémoire conserve une seule valeur et reste disponible après un effacement de l'affichage.

En cas de division par zéro, l'interface affiche `Erreur`.

### Historique

Le bouton **Historique** ouvre une fenêtre dédiée contenant les calculs effectués pendant la session et devient alors **Fermer Historique**. Un nouvel appui ferme la fenêtre et rétablit le bouton **Historique**. Si la fenêtre est fermée directement, le bouton revient également à **Historique**.

La fenêtre d'historique reste rattachée à la fenêtre principale : son coin supérieur droit coïncide avec le coin supérieur gauche de celle-ci et elle suit ses déplacements. Elle se ferme automatiquement lorsque la fenêtre principale est fermée.

Le bouton **Effacer l'historique** supprime toutes les entrées de la session.

## Architecture fonctionnelle

La logique de calcul est distincte de l'interface graphique. Cela permet de tester les opérations indépendamment de PySide6 et limite le risque de régression lors des évolutions de l'interface.
