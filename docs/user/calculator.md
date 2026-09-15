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
- gestion de la division par zéro.

Les calculs utilisent `Decimal` afin d'éviter les imprécisions usuelles des calculs flottants binaires pour les valeurs décimales saisies par l'utilisateur.

## Utilisation

La saisie se fait avec les boutons de la fenêtre :

- les chiffres permettent de construire le nombre courant ;
- `.` saisit le séparateur décimal ;
- `+`, `-`, `×` et `÷` sélectionnent l'opération ;
- `=` calcule le résultat ;
- `C` efface la saisie et réinitialise l'état ;
- `⌫` supprime le dernier caractère ;
- `±` inverse le signe du nombre courant.

En cas de division par zéro, l'interface affiche `Erreur`.

## Architecture fonctionnelle

La logique de calcul est distincte de l'interface graphique. Cela permet de tester les opérations indépendamment de PySide6 et limite le risque de régression lors des évolutions de l'interface.
