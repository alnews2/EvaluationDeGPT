# Build Windows

## Principe

Le build officiel de l'application Windows est réalisé par GitHub Actions avec PyInstaller.

La CI :

1. utilise Windows ;
2. installe Python 3.13 ;
3. installe les dépendances du projet et les outils de build ;
4. exécute Ruff ;
5. exécute pytest ;
6. construit `EvaluationDeGPT.exe` avec PyInstaller ;
7. publie l'exécutable comme artefact GitHub Actions.

## Point d'entrée PyInstaller

Le build utilise :

```text
src/evaluation_de_gpt/__main__.py
```

et non `main.py` directement. Ce choix est important car `main.py` appartient au package et utilise ses imports dans ce contexte.

La commande de référence est :

```text
pyinstaller --noconfirm --clean --onefile --windowed --name EvaluationDeGPT src/evaluation_de_gpt/__main__.py
```

Le fichier obtenu est :

```text
dist/EvaluationDeGPT.exe
```

## Validation

Un build réussi ne constitue pas à lui seul une validation fonctionnelle complète. Après une évolution de l'application, l'exécutable doit être testé lorsque le changement peut affecter le comportement utilisateur.
