# Historique Discord

## Introduction
Ce projet de bot Discord fait pour l'école, permettant d'avoir plusieurs fonctionalités communautaire.

## Fonctionnalités

### Commandes d'historique
- `$hdc`: Affiche la dernière commande d'un utilisateur.
- `$htc`: Affiche toutes les commandes d'un utilisateur.
- `$hdm`: Affiche le dernier message d'un utilisateur.
- `$htm`: Affiche tous les messages d'un utilisateur.
- `$htid`: Affiche tous les messages et toutes les commandes d'un utilisateur.
- `$vhmid`: Vide l'historique des messages d'un utilisateur.
- `$vhcid`: Vide l'historique des commandes d'un utilisateur.
- `$vhid`: Vide l'historique complet d'un utilisateur.

### Autres commandes
- `$bienvenue`: Définit le salon de bienvenue.
- `$clear`: Supprime un nombre donné de messages.
- `$pfc`: Pierre, feuille, ciseaux avec l'ordinateur.
- `$sendhelp`: Commencer une conversation arborescente.
- `$avatar`: Affiche l'avatar d'un membre.
- `$aide`: Affiche la liste des commandes disponibles.
- `$pendu` : Lance le jeu du pendu 

## Implémentation
Ce bot utilise une base de données SQL pour stocker l'historique des commandes et des messages des utilisateurs.

## Arborescence de dossiers
- `token_1.py`: Fichier contenant le jeton pour le bot.
- `historique.db`: Base de données SQLite pour stocker les historiques et diverses choses afin de facilité ma gestion des données.
- `commande_historique.py`: Script contenant des classes pour gérer l'historique des commandes et des messages.
- `tree.py`: Script contenant la structure de données pour une conversation arborescente.

## Commandes de test
Des commandes de test (`$prout`, `$send`, etc.) sont incluses pour faciliter les tests du bot.

## Difficultés Rencontrées

### Gestion du Projet

1. **Planification du Projet**: Définir clairement les étapes de développement et les fonctionnalités à implémenter.
2. **Gestion du Temps**: La procrastination est mauvaise pour la santé :/
3. **Intégration de Discord.py**: Comprendre et maîtriser les fonctionnalités de la librairie Discord.py pour créer un bot Discord interactif.
4. **Tests et Débogage**: Identifier et résoudre les erreurs rencontrés lors du développement du bot (Parfois incompréhensible xD).
5. **Gérer le multi-serveur** : Au dernier moment se rendre compte qu'il faut aussi gérer le fait que le bot, puisse être dans différents serveurs, donc gérer les utilisateurs pour chaques serveurs etc... Faire des Hashmap de Hashmap pour trier par serveur et ensuite par ID utilisateur ... (Pas totalement fini )

### Développement Technique

1. **Gestion des Données**: Stocker et gérer les données qu'on reçoit.
2. **Affichage de l'Information**: Gérer l'affichage des informations dans Discord pour éviter les problèmes de formatage.
3. **Intégration d'Images**: Intégrer des images pour illustrer le pendu ou les étapes du jeu.
4. **Interaction Utilisateur**: S'assurer que le bot réagit correctement aux actions et aux commandes des utilisateurs.


Le problème principal que j'ai rencontré au long de ce projet c'est de structurer mes idées, de savoir se que je peux faire pour parvenir à vos attentes, et de voir comment y parvenir ou même comprendre concrètement se que vous souhaitez  

# Je pense continuer à développer ce bot pour faire un bon bot communautaire !

---

