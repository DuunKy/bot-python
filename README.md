# Historique Discord

## Introduction
Ce projet de bot Discord a été développé pour enregistrer et afficher l'historique des commandes et des messages des utilisateurs sur un serveur Discord.

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

## Implémentation
Ce bot utilise une base de données SQLite pour stocker l'historique des commandes et des messages des utilisateurs. Il s'agit d'un bot Discord développé en Python à l'aide de la bibliothèque `discord.py`.

## Arborescence de dossiers
- `token_1.py`: Fichier contenant le jeton pour le bot.
- `historique.db`: Base de données SQLite pour stocker les historiques.
- `commande_historique.py`: Script contenant des classes pour gérer l'historique des commandes et des messages.
- `tree.py`: Script contenant la structure de données pour une conversation arborescente.

## Commandes de test
Des commandes de test (`$prout`, `$send`, etc.) sont incluses pour faciliter les tests du bot.

---

