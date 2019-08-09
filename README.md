# Project 3
> Aidez MacGyver à s'échapper !


Étant un grand fan de Richard Dean Anderson, vous imaginez un labyrinthe 2D dans lequel MacGyver aurait été enfermé. La sortie est surveillée par un garde du corps dont la coiffure ferait pâlir Tina Turner.
Pour le distraire, il vous faut réunir les éléments suivants (dispersés dans le labyrinthe): une aiguille, un petit tube en plastique et de l'éther.
Ils permettront à MacGyver de créer une seringue et d'endormir notre garde.

![gif](demo.gif)

Le jeu se joue avec les touches directionnelles.
Si vous touchez le gardien avec moins d'un objet à la main vous mourrez
Si vous touchez le gardien sans objet, il ne vous tuera

## Installation

téléchargez le jeu à partir de Github puis selon OS, à partir du fichier racine:

OS X & Linux:

```sh
npm install
```

Windows:

```sh
pip
```


_For more examples and usage, please refer to the [Wiki][wiki]._

## Changelog

### Version 0.1:

  * pas de grahique, le terrain se dessine dans l'invité de commande et les
    les positions des objet et celui du héros
  * main.py fonctionne et le héros se deplace
  * l'environnement se charge et les 3 objets sont positioner aleatoirement
  * arret du jeu apres 10 appuie sur une touche ou la touche "1"

### Version 0.2:

  1. ajout de la fonction de recuperation des objets
  2. ajout de la fonction qui determine si le héros rencontre un mur
  3. nettoyage du code dans Environment.py
  4. re-codage de main.py afin de faire fonctionner les 2 modules ensemble

### Version 0.3:

  1. ajout du graphique en stand alone
  2. ajout des fonctions qui dessine l'arriere plan, les murs, le héros, les outils
  3. ajout de la fonction deplacement du héros en graphique (stand alone)

### Version 0.4:

  1. le jeu fonction en mode graphique

### Version 0.5:

  1. definition de la position initiale du héros depuis le dessin
        du labyrinthe
  2. dessin du gardian dans le jeu graphique
  3. Verification du standard PEP8 sur tout les fichiers
  4. ajout de la condition pour gagner le jeu

### Version 0.6:

  1. le labyrinthe est chargé depuis un fichier texte
  2. Pour chaque objet, il lui est attribué une image dediée

### Version 0.7:

  1. le jeu demarre a partir de main.py uniquement

### Version 1.0:

  1. le jeu peux demarrer soit en mode graphique soit en mode commande
  2. ajout d'un ecran de fin

### Version 1.1:

  1. Ajout d'un ecran de perdu
  2. amelioration du code
  3. Ajout d'une possibilité de perdre
  4. ajout d'un compteur d'objet

## To-Do list

  - [x] Rajouter un ecran de fin.
  - [ ] Rajouter du son.
  - [ ] Trouver de meilleurs images.



<!-- Markdown link & img dfn's -->

[wiki]: https://i.skyrock.net/2059/12582059/pics/311796304_small.jpg
