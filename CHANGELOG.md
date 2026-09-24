# Changelog

Toutes les modifications notables de l'application sont documentées dans ce fichier.

Le format est inspiré de [Keep a Changelog](https://keepachangelog.com/).
Les versions suivent le versionnement sémantique (SemVer).

## [Unreleased]

## [0.5.1] - 2026-09-24

### Changed

- fix: abaisser l'affichage de la mémoire

### Changed

- Abaissement d’environ 5 mm de la zone d’affichage du contenu de la mémoire dans la fenêtre principale.

## [0.5.0] - 2026-09-24

### Changed

- feat: rattacher la fenêtre historique à la fenêtre principale

### Changed

- La fenêtre d'historique est maintenant rattachée à la fenêtre principale, avec son coin supérieur droit aligné sur le coin supérieur gauche de celle-ci, et se ferme avec elle.

## [0.4.0] - 2026-09-23

### Changed

- feat: ajouter l'historique des calculs

### Added

- Ajout d'une fenêtre dédiée affichant l'historique des calculs effectués pendant la session.
- Ajout de la possibilité d'effacer l'historique des calculs.

### Fixed

- Correction de la largeur du bouton « Historique » afin que son libellé soit entièrement visible.

## [0.3.0] - 2026-09-17

### Changed

- feat: afficher la mémoire en permanence

### Added

- Affichage permanent du contenu de la mémoire sous l'écran principal de la calculatrice.
- Indication `—` lorsqu'aucune valeur n'est mémorisée.

## [0.2.0] - 2026-09-17

### Changed

- feat: mémoriser et restituer un nombre

### Added

- Mémorisation du nombre affiché avec la touche `M`.
- Restitution du nombre mémorisé avec la touche `MR`, comme une saisie clavier.

## [0.1.0] - 2026-09-15

### Added

- Première version de l'application.
- Calculatrice quatre opérations avec interface graphique PySide6.
- Addition, soustraction, multiplication et division.
- Gestion des nombres décimaux.
- Changement de signe.
- Effacement et retour arrière.
- Gestion de la division par zéro.
- Tests automatisés avec pytest.
- Vérification du code avec Ruff.
- Construction d'un exécutable Windows avec GitHub Actions et PyInstaller.
- Attribution de l'utilisation de GPT par OpenAI dans l'interface.
