# Project 3



Version 0.1:

  * pas de grahique, le terrain se dessine dans l'invité de commande et les
    les positions des objet et celui du hero
  * main.py fonctionne et le hero se deplace
  * l'environnement se charge et les 3 objets sont positioner aleatoirement
  * arret du jeu apres 10 appuie sur une touche ou la touche "1"

--> difficulté: mettre a jour l'affichage non grahique avec le deplacement
      du héro et des objets

--> prochaine étape :

    - donner la fonction au hero de rammasser des objets
    - une fonction qui empeche le hero de traverser les murs

Version 0.2:
* pas de grahique, le terrain se dessine dans l'invité de commande et  
  les positions des objets et celui du hero
* main.py fonctionne et le hero se deplace et recupere les objets et ne se
  deplace pas dans les murs
* arret du jeu apres 100 appuie sur une touche ou la touche "1" ou les
  3 objets recuperés

  ###### Nouvauté ######
  ** ajout de la fonction de recuperation des objets
  ** ajout de la fonction qui determine si le hero rencontre un mur
  ** nettoyage du code dans Environment.py
  ** re-codage de main.py afin de faire fonctionner les 2 modules ensemble
  ######          ######

  --> difficulté: utilisation de la fonction super() pour recuperé un attribut
  d'une class parente

  --> prochaine étape :

    - definir la position du hero en fonction du dessin du labyrinthe
    - interface graphique

Version 0.3:
  * graphique fonctionne en stand alone
  * main.py fonctionne (sans graphique) et le hero se deplace et recupere les objets et ne se
      deplace pas dans les murs (le terrain se dessine dans l'invité de commande et  
        les positions des objets et celui du hero)
  * arret du jeu apres 100 appuie sur une touche ou la touche "1" ou les
      3 objets recuperés (version command)

  ###### Nouvauté ######
      ** ajout du graphique en stand alone **
      ** ajout des fonctions qui dessine l'arriere plan, les murs, le hero, les outils
      ** ajout de la fonction deplacement du hero en graphique (stand alone)

  ######          ######

  --> difficulté: utilisation du module pygame

  --> prochaine étape :

      - definir la position du hero en fonction du dessin du labyrinthe
      - tranformer les fontion du graphic en class
      - lier l'interface graphique au reste des classes
