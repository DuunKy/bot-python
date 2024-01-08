import random
import discord
import sqlite3
import os
intents = discord.Intents.all()
from discord.ext import commands
from discord.utils import get
from discord.ui import Select
import commande_historique
import tree
import	token_1

client = commands.Bot(command_prefix="$", intents = intents)


# Pour les sauvegardes 

historique_utilisateur_commandes = {}
historique_utilisateur_messages = {}
Utilisateur = []
file_attente =[]

conn = sqlite3.connect('historique.db')
cursor = conn.cursor()

# Récupération des ID d'utilisateurs dans la table Commandes et Messages

cursor.execute("SELECT DISTINCT user_id FROM Utilisateurs")
user_ids = cursor.fetchall()

# On met en liste chaînée  pour chaque utilisateur

for user_id in user_ids:
    historique_utilisateur_commandes[user_id[0]] = commande_historique.chained_list()
    historique_utilisateur_messages[user_id[0]] = commande_historique.chained_list()
    Utilisateur.append(str(user_id[0]))
    
    
    
# Récupération des commandes et des messages dans les tables respectives

cursor.execute("SELECT user_id, command_text FROM Commandes")
rows_commandes = cursor.fetchall()
cursor.execute("SELECT user_id, message_content FROM Messages")
rows_messages = cursor.fetchall()

# Ajout des commandes et des messages à la liste chaînée correspondante dans historique_utilisateur
for row in rows_commandes:
    user_id, command_text = row
    historique_utilisateur_commandes[user_id].append(command_text)
for row in rows_messages:
    user_id, message_content = row
    historique_utilisateur_messages[user_id].append(message_content)
    
              
# ----------------------------------------------


# Les commandes pour l'historique

@client.command(name="hdc")
async def d_commande(ctx):
    file_attente.append(ctx.author.id)
    
    if file_attente[0] is not ctx.author.id:
      await ctx.send("Un utilisateur accède déjà à l'historique, veuillez patienter.", delete_after=5.0)
      return
    

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    while True:
        await ctx.send("Entrez un ID ou 'exit' pour quitter")
        msg = await client.wait_for("message", check=check)
        if msg.content.lower() == "exit":
            await ctx.send("Vous quittez la commande", delete_after=3.0)
            file_attente.remove(ctx.author.id)
            return

        try:
            id = int(msg.content)
            member = ctx.guild.get_member(id)
            if not member:
                await ctx.send("ID invalide, réessayez ou tapez 'exit' pour quitter.")
                continue

            user_id = member.id
            user_name = member.name
            derniere_commande = historique_utilisateur_commandes[user_id].derniere()
            await ctx.send(f"Dernière commande de {user_name} : {derniere_commande}",delete_after=20.0)
            cursor.execute("INSERT INTO Commandes (user_id, command_text) VALUES (?, ?)", (ctx.author.id, "$hdc "+msg.content))
            conn.commit()
        except ValueError:
            await ctx.send("Entrez un ID valide ou 'exit' pour quitter.")
    
   
@client.command(name="htc")
async def t_commandes(ctx):
  
  file_attente.append(ctx.author.id)
  
  if file_attente[0] is not ctx.author.id:
    await ctx.send("Un utilisateur accède déjà à l'historique, veuillez patienter.", delete_after=5.0)
    return
  
  await ctx.send("Entrez un ID ou 'exit' pour quitter")
  
  def check(m):
      return m.author == ctx.author and m.channel == ctx.channel

  while True:
     msg = await client.wait_for("message", check=check)
     if msg.content.lower() == "exit":
        await ctx.send("Vous quittez la commande", delete_after=3.0)
        file_attente.pop()
        return

     try:
         id = int(msg.content)
         member = ctx.guild.get_member(id)
         if not member:
                await ctx.send("ID invalide, réessayez ou tapez 'exit' pour quitter.")
                continue

         user_id = member.id
         user_name = member.name
         toutes_commandes = historique_utilisateur_commandes[user_id].tout_afficher()
         await ctx.send(f"Toutes les commandes de {user_name} : {toutes_commandes}", delete_after=20.0)
         historique_utilisateur_commandes[ctx.author.id].append("$htc "+msg.content)
         cursor.execute("INSERT INTO Commandes (user_id, command_text) VALUES (?, ?)", (ctx.author.id, "$htc "+msg.content))
         conn.commit()
     except ValueError:
            await ctx.send("Entrez un ID valide ou 'exit' pour quitter.")
     
 
@client.command(name="hdm")
async def d_messages(ctx):
  
  file_attente.append(ctx.author.id)
  
  if file_attente[len(file_attente)-1] is not ctx.author.id:
    await ctx.send("Un utilisateur accède déjà à l'historique, veuillez patienter.", delete_after=5.0)
    return
  
  
  def check(m):
      return m.author == ctx.author and m.channel == ctx.channel

  while True:
     await ctx.send("Entrez un ID ou 'exit' pour quitter")
     
     msg = await client.wait_for("message", check=check)
     
     if msg.content.lower() == "exit":
        await ctx.send("Vous quittez la commande", delete_after=3.0)
        file_attente.pop()
        return

     try:
         id = int(msg.content)
         member = ctx.guild.get_member(id)
         if not member:
                await ctx.send("ID invalide, réessayez ou tapez 'exit' pour quitter.")
                continue

         user_id = member.id
         user_name = member.name
         dernier_messages = historique_utilisateur_messages[user_id].derniere()
         await ctx.send(f"Dernier message de {user_name} : {dernier_messages}", delete_after=20.0)
         historique_utilisateur_commandes[ctx.author.id].append("$hdm "+msg.content)
         cursor.execute("INSERT INTO Commandes (user_id, command_text) VALUES (?, ?)", (ctx.author.id, "$hdm "+msg.content))
         conn.commit()
     except ValueError:
            await ctx.send("Entrez un ID valide ou 'exit' pour quitter.")
  
  
@client.command(name="htm")
async def h_messages(ctx):
  
  file_attente.append(ctx.author.id)
  
  if file_attente[0] is not ctx.author.id:
    await ctx.send("Un utilisateur accède déjà à l'historique, veuillez patienter.", delete_after=5.0)
    return
  
  def check(m):
      return m.author == ctx.author and m.channel == ctx.channel

  while True:
     await ctx.send("Entrez un ID ou 'exit' pour quitter")
     msg = await client.wait_for("message", check=check)
     
     if msg.content.lower() == "exit":
        await ctx.send("Vous quittez la commande", delete_after=3.0)
        file_attente.remove(ctx.author.id)
        return

     try:
         id = int(msg.content)
         member = ctx.guild.get_member(id)
         if not member:
                await ctx.send("ID invalide, réessayez ou tapez 'exit' pour quitter.")
                continue

         user_id = member.id
         user_name = member.name
         tout_messages = historique_utilisateur_messages[user_id].tout_afficher()
         await ctx.send(f"Tous les messages de {user_name} : {tout_messages}", delete_after=20.0)
         historique_utilisateur_commandes[ctx.author.id].append("$htm "+msg.content)
         cursor.execute("INSERT INTO Commandes (user_id, command_text) VALUES (?, ?)", (ctx.author.id, "$htm "+msg.content))
         conn.commit()
     except ValueError:
            await ctx.send("Entrez un ID valide ou 'exit' pour quitter.")
  
  
@client.command(name="htid")
async def h_tout(ctx):
  file_attente.append(ctx.author.id)
  
  if file_attente[0] is not ctx.author.id:
    await ctx.send("Un utilisateur accède déjà à l'historique, veuillez patienter.", delete_after=5.0)
    return
  
  def check(m):
      return m.author == ctx.author and m.channel == ctx.channel

  while True:
     await ctx.send("Entrez un ID ou 'exit' pour quitter")
     msg = await client.wait_for("message", check=check)
     
     if msg.content.lower() == "exit":
        await ctx.send("Vous quittez la commande", delete_after=3.0)
        file_attente.remove(ctx.author.id)
        return

     try:
         id = int(msg.content)
         member = ctx.guild.get_member(id)
         if not member:
                await ctx.send("ID invalide, réessayez ou tapez 'exit' pour quitter.")
                continue

         user_id = member.id
         user_name = member.name
         tout_messages = historique_utilisateur_messages[user_id].tout_afficher()
         await ctx.send(f"Tous les messages de {user_name} : {tout_messages}",delete_after=20.0)
         await ctx.send(f"---------------------------------------------",delete_after=20.0)
         toutes_commandes = historique_utilisateur_commandes[user_id].tout_afficher()
         await ctx.send(f"Toutes les commandes de {user_name} : {toutes_commandes}",delete_after=20.0)
         historique_utilisateur_commandes[ctx.author.id].append("$htid "+msg.content)
         cursor.execute("INSERT INTO Commandes (user_id, command_text) VALUES (?, ?)", (ctx.author.id, "$htid "+msg.content))
         conn.commit()
     except ValueError:
            await ctx.send("Entrez un ID valide ou 'exit' pour quitter.")


@client.command(name="vhmid")
async def vider_historique_messages(ctx):
  file_attente.append(ctx.author.id)
  
  if file_attente[0] is not ctx.author.id:
    await ctx.send("Un utilisateur accède déjà à l'historique, veuillez patienter.", delete_after=5.0)
    return
  
  def check(m):
      return m.author == ctx.author and m.channel == ctx.channel

  while True:
     await ctx.send("Entrez un ID ou 'exit' pour quitter")
     msg = await client.wait_for("message", check=check)
     
     if msg.content.lower() == "exit":
        await ctx.send("Vous quittez la commande", delete_after=3.0)
        file_attente.remove(ctx.author.id)
        return

     try:
         id = int(msg.content)
         member = ctx.guild.get_member(id)
         if not member:
                await ctx.send("ID invalide, réessayez ou tapez 'exit' pour quitter.")
                continue

         user_id = member.id
         user_name = member.name
         historique_utilisateur_messages[user_id].vider()
         await ctx.send(f"Historique des messages de l'utilisateur {user_name} vidé !", delete_after=4.0)
         historique_utilisateur_commandes[ctx.author.id].append("$vhmid "+msg.content)
         cursor.execute("INSERT INTO Commandes (user_id, command_text) VALUES (?, ?)", (ctx.author.id, "$vhmid "+msg.content))
         conn.commit()
     except ValueError:
            await ctx.send("Entrez un ID valide ou 'exit' pour quitter.")


@client.command(name="vhcid")
async def vider_historique_commandes(ctx):
  file_attente.append(ctx.author.id)
  
  if file_attente[0] is not ctx.author.id:
    await ctx.send("Un utilisateur accède déjà à l'historique, veuillez patienter.", delete_after=5.0)
    return
  
  def check(m):
      return m.author == ctx.author and m.channel == ctx.channel

  while True:
     await ctx.send("Entrez un ID ou 'exit' pour quitter")
     msg = await client.wait_for("message", check=check)
     
     if msg.content.lower() == "exit":
        await ctx.send("Vous quittez la commande", delete_after=3.0)
        file_attente.remove(ctx.author.id)
        return

     try:
         id = int(msg.content)
         member = ctx.guild.get_member(id)
         if not member:
                await ctx.send("ID invalide, réessayez ou tapez 'exit' pour quitter.")
                continue

         user_id = member.id
         user_name = member.name
         historique_utilisateur_commandes[user_id].vider()
         await ctx.send(f"Historique des commandes de l'utilisateur {user_name} vidé !", delete_after=4.0)
         historique_utilisateur_commandes[ctx.author.id].append("$vhcid "+msg.content)
         cursor.execute("INSERT INTO Commandes (user_id, command_text) VALUES (?, ?)", (ctx.author.id, "$vhcid "+msg.content))
         conn.commit()
     except ValueError:
            await ctx.send("Entrez un ID valide ou 'exit' pour quitter.")
  
  
@client.command(name="vhid")
async def vider_historique(ctx):
  file_attente.append(ctx.author.id)
  
  if file_attente[0] is not ctx.author.id:
    await ctx.send("Un utilisateur accède déjà à l'historique, veuillez patienter.", delete_after=5.0)
    return
  
  def check(m):
      return m.author == ctx.author and m.channel == ctx.channel

  while True:
     await ctx.send("Entrez un ID ou 'exit' pour quitter")
     msg = await client.wait_for("message", check=check)
     
     if msg.content.lower() == "exit":
        await ctx.send("Vous quittez la commande", delete_after=3.0)
        file_attente.remove(ctx.author.id)
        return

     try:
         id = int(msg.content)
         member = ctx.guild.get_member(id)
         if not member:
                await ctx.send("ID invalide, réessayez ou tapez 'exit' pour quitter.")
                continue

         user_id = member.id
         user_name = member.name
         historique_utilisateur_messages[user_id].vider()
         historique_utilisateur_commandes[user_id].vider()
         await ctx.send(f"Historique d'{user_name} vidé !", delete_after=4.0)
         historique_utilisateur_commandes[ctx.author.id].append("$vhid "+msg.content)
         cursor.execute("INSERT INTO Commandes (user_id, command_text) VALUES (?, ?)", (ctx.author.id, "$vhid "+msg.content))
         conn.commit()
     except ValueError:
            await ctx.send("Entrez un ID valide ou 'exit' pour quitter.")
  
# ----------------------------------------------

#Autres fonctionalistés

@client.command(name="clear")
async def delete(message, amount: int):
    await message.channel.purge(limit=amount+1)
    await message.channel.send("Messages supprimés !", delete_after=3.0)
    
@client.command(name="bienvenue")
async def bienvenue(ctx):
    channel = client.get_channel(ctx.message.channel.id)
    if channel:
        # Vérifie si l'utilisateur a les permissions nécessaires
        if ctx.author.guild_permissions.manage_channels:
            # Enregistre l'ID du salon de bienvenue dans une base de données ou un fichier
            cursor.execute("UPDATE Serveurs SET channel_bienvenue = ? WHERE server_id = ?", (channel.id, ctx.guild.id))
            conn.commit()
            await ctx.send(f"Le salon de bienvenue est maintenant {channel.mention}",delete_after=5.0)
        else:
            await ctx.send("Désolé, vous n'avez pas la permission de gérer les salons.")
    else:
        await ctx.send("Canal introuvable.")

@client.command()
async def avatar(ctx, member: discord.Member):
    await ctx.send(f"{member.display_avatar}")

@client.command()
async def aide(ctx):
    embed = discord.Embed(
        title="Liste des commandes disponibles",
        description="Voici la liste des commandes disponibles sur ce bot",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=ctx.author.display_avatar)
    embed.set_footer(text=f"Commande demandée par {ctx.author.name}")
    embed.add_field(name="$bienvenue", value="Définit le salon de bienvenue", inline=False)
    embed.add_field(name="$hdc", value="Affiche la dernière commande d'un utilisateur", inline=False)
    embed.add_field(name="$htc", value="Affiche toutes les commandes d'un utilisateur", inline=False)
    embed.add_field(name="$hdm", value="Affiche le dernier message d'un utilisateur", inline=False)
    embed.add_field(name="$htm", value="Affiche tous les messages d'un utilisateur", inline=False)
    embed.add_field(name="$htid", value="Affiche tous les messages et toutes les commandes d'un utilisateur", inline=False)
    embed.add_field(name="$vhmid", value="Vide l'historique des messages d'un utilisateur", inline=False)
    embed.add_field(name="$vhcid", value="Vide l'historique des commandes d'un utilisateur", inline=False)
    embed.add_field(name="$vhid", value="Vide l'historique d'un utilisateur", inline=False)
    embed.add_field(name="$clear", value="Supprime un nombre de messages donné", inline=False)
    await ctx.send(embed=embed)
# ----------------------------------------------

# Petits jeux

# Marche pas
@client.command()
async def pfc(ctx):
  select = Select(
    placeholder="Pierre, feuille, ciseaux",
    options=[
    discord.SelectOption(label="Pierre", description="Vous choisissez la Pierre", emoji="✊"),
    discord.SelectOption(label="Feuille", description="Vous choisissez la Feuille", emoji="✋"),
    discord.SelectOption(label="Ciseaux", description="Vous choisissez le Ciseaux", emoji="✌️")
  ])
  view= discord.ui.View()
  view.add_item(select)
  await ctx.send("Pierre, feuille, ciseaux ?", view=view)
  await ctx.send(f"Vous avez choisi {select.selected_options[0].label}")
  await ctx.send("L'ordinateur choisit...")
  await ctx.send("3...")
  await ctx.send("2...")
  await ctx.send("1...")
  await ctx.send("...")
  # 0 = Pierre, 1 = Feuille, 2 = Ciseaux
  choix_ordinateur = random.randint(0,2)
  if choix_ordinateur == 0:
    await ctx.send("L'ordinateur a choisi Pierre !")
  elif choix_ordinateur == 1:
    await ctx.send("L'ordinateur a choisi Feuille !")
  else:
    await ctx.send("L'ordinateur a choisi Ciseaux !")
  if select.selected_options[0].label == "Pierre":
    if choix_ordinateur == 0:
      await ctx.send("Egalité !")
    elif choix_ordinateur == 1:
      await ctx.send("Vous avez perdu !")
    else:
      await ctx.send("Vous avez gagné !")
  elif select.selected_options[0].label == "Feuille":
    if choix_ordinateur == 0:
      await ctx.send("Vous avez gagné !")
    elif choix_ordinateur == 1:
      await ctx.send("Egalité !")
    else:
      await ctx.send("Vous avez perdu !")
  else:
    if choix_ordinateur == 0:
      await ctx.send("Vous avez perdu !")
    elif choix_ordinateur == 1:
      await ctx.send("Vous avez gagné !")
    else:
      await ctx.send("Egalité !")
  


@client.command()
async def pendu(ctx):
    liste_mots = ["Banane", "Ordinateur", "Tigre", "Avion", "Piano", "Cascade", "Chocolat", "Fusee", "Montagne", "Etoile"]

    while True:
        mot_caché = random.choice(liste_mots).lower()
        mot_caché_affichage = ["_" for _ in mot_caché]

        embed_pendu_bienvenue = discord.Embed(
            title="Le Pendu !",
            description=f"Bienvenue dans le jeu du pendu !\nVous avez 8 essais pour trouver le mot caché! \n Bonne chance !",
            color=0x00ffff
        )
        await ctx.send(embed=embed_pendu_bienvenue)

        essais = 8
        image = 1

        while essais > 0:
            mot_caché_affichage_str = " ".join(mot_caché_affichage)
            
            embed_pendu = discord.Embed(
                title=f"Le Pendu ! - Essai n°{9 - essais}",
                description=f"Vous avez {essais} essais pour trouver le mot caché\nLe mot caché est : ```{mot_caché_affichage_str}```",
                color=0x00ffff
            )
            embed_pendu.set_image(url="https://st3.depositphotos.com/11514374/17116/v/380/depositphotos_171164736-stock-illustration-drawing-of-hang-knot-noose.jpg")
            await ctx.send(embed=embed_pendu)
            await ctx.send("Entrez une lettre")
            
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            lettre = (await client.wait_for("message", check=check)).content.lower()
            
            if lettre == "exit":
                await ctx.send("Vous quittez le jeu du pendu", delete_after=5.0)
                break 

            if lettre in mot_caché:
                await ctx.send("Bien joué !")
                for i in range(len(mot_caché)):
                    if mot_caché[i] == lettre:
                        mot_caché_affichage[i] = lettre
                await ctx.send(" ".join(mot_caché_affichage))
                if "_" not in mot_caché_affichage:
                    await ctx.send("Vous avez gagné !")
                    break
            else:
                await ctx.send("Raté !")
                essais -= 1
                image += 1
                await ctx.send(f"Il vous reste {essais} essais")
                
        if essais == 0:
            await ctx.send(f"Vous avez perdu ! Le mot était : {mot_caché}")

        await ctx.send("Voulez-vous rejouer ? (oui/non)")
        rejouer = (await client.wait_for("message", check=check)).content.lower()
        if rejouer == "non":
            await ctx.send("Vous quittez le jeu du pendu, merci d'avoir joué", delete_after=5.0)
            break
        else:
            await ctx.send("C'est reparti !")





      
    
@client.command(name="sendhelp")
async def help_command(ctx):
    question = tree.Discussion.get_questionTree()
    await ctx.send((f"Parlons un peu! \n Répondez avec'$send 1' or '$send 2' or '$send reset' pour recommencer.\n{question}"))

@client.command(name="send")
async def answer_command(ctx, answer):
    response = tree.Discussion.send_answerTree(answer)
    await ctx.send((response))


       

# ----------------------------------------------



# Commandes nulles pour tester

@client.command(name="prout")
async def prout(ctx):
    await ctx.send("prout")

# ----------------------------------------------   





# Lancement du bot

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Cette commande est inconnue. Tapez $aide pour avoir la liste des commandes disponibles.", delete_after=5.0)


@client.event
async def on_ready():
    for guild in client.guilds:
        server_id = guild.id
        server_name = guild.name

        # Vérification si le serveur existe déjà dans la table
        cursor.execute("SELECT * FROM Serveurs WHERE server_id = ?", (server_id,))
        server_exists = cursor.fetchone()

        # Si le serveur n'existe pas, l'insérer dans la table
        if not server_exists:
            cursor.execute("INSERT INTO Serveurs (server_id, server_name) VALUES (?, ?)", (server_id, server_name))
            conn.commit()
            print(f"Serveur ajouté à la DB : {server_id}")

        # Pour chaque membre sur le serveur
        for member in guild.members:
            user_id = member.id
            user_name = member.name

            # Vérifie si l'utilisateur existe déjà dans la table Utilisateurs
            cursor.execute("SELECT * FROM Utilisateurs WHERE user_id = ?", (user_id,))
            user_exists = cursor.fetchone()

            # Si l'utilisateur n'existe pas, l'insérer dans la table Utilisateurs
            if not user_exists:
                cursor.execute("INSERT INTO Utilisateurs (user_id, username) VALUES (?, ?)", (user_id, user_name))
                conn.commit()
                print(f"Utilisateur ajouté à la DB : {user_id}")

            # Vérifie si l'utilisateur est déjà dans la table Utilisateurs_Serveurs pour ce serveur
            cursor.execute("SELECT * FROM Utilisateurs_Serveurs WHERE user_id = ? AND server_id = ?", (user_id, server_id))
            user_exists_server = cursor.fetchone()

            # Si l'utilisateur n'existe pas pour ce serveur, l'insérer dans la table Utilisateurs_Serveurs
            if not user_exists_server:
                cursor.execute("INSERT INTO Utilisateurs_Serveurs (user_id, server_id) VALUES (?, ?)", (user_id, server_id))
                conn.commit()
                print(f"Utilisateur ajouté à la DB : {user_id} sur le serveur {server_id}")

    print("Let's gooooooo!")



@client.event
async def on_member_join(member):
  user_id = member.id
  user_name = member.name
  server_id = member.guild.id
  
  cursor.execute("SELECT channel_bienvenue FROM Serveurs WHERE server_id = ?", (server_id,))
  channel_id = cursor.fetchone()[0]
  
  
  cursor.execute("SELECT * FROM Utilisateurs WHERE user_id = ?", (user_id,))
  user_exists = cursor.fetchone()
  
  # Si l'utilisateur n'existe pas, l'insérer dans la table
  if not user_exists:
    cursor.execute("INSERT INTO Utilisateurs (user_id,username) VALUES (?, ?)", (user_id,user_name))
    conn.commit()
    cursor.execute("INSERT INTO Utilisateurs_Serveurs (user_id, server_id) VALUES (?, ?)", (user_id, member.guild.id))
    conn.commit()
    print(f"Utilisateur ajouté à la base de données : {user_id}")
    
    
  bienvenue_channel = get(client.get_all_channels(),id=channel_id)
  
  # Si il n'y a pas de salon de bienvenue, ne rien faire
  if not channel_id:
    return
  
  embed = discord.Embed(
        title=f"Bienvenue sur le serveur, {member.name}!",
        description="Salut grand fou bienvenue sur le serveur installe toi !\n\nPour avoir la liste des commandes disponibles, tapez $aide",
        color=discord.Color.blue()
    )
  embed.set_thumbnail(url=member.display_avatar)
  embed.set_footer(text=f"Merci de rejoindre notre communauté, {member.name}!")
  await bienvenue_channel.send(embed=embed)
  



@client.event
async def on_message(message):
  
  
  if message.author == client.user:
    return

  message.content = message.content.lower()
  
 
  if not message.content.startswith("$") and message.content not in Utilisateur and not message.content.startswith("exit"):
    if message.author.id not in historique_utilisateur_messages:
      historique_utilisateur_messages[message.author.id] = commande_historique.chained_list()
      historique_utilisateur_messages[message.author.id].append(message.content)
      cursor.execute("INSERT INTO Messages (user_id,channel_id,message_content,server_id) VALUES (?, ?, ?, ?)",(message.author.id, message.channel.id, message.content, message.guild.id))
      conn.commit()
    else:
      historique_utilisateur_messages[message.author.id].append(message.content)
      cursor.execute("INSERT INTO Messages (user_id,channel_id,message_content,server_id) VALUES (?, ?, ?, ?)",(message.author.id, message.channel.id, message.content, message.guild.id))
      conn.commit()
    


  if message.content.startswith("$") and "hdc" not in message.content:
    if message.author.id not in historique_utilisateur_commandes:
      historique_utilisateur_commandes[message.author.id] = commande_historique.chained_list()
    historique_utilisateur_commandes[message.author.id].append(message.content)
    cursor.execute("INSERT INTO Commandes (user_id, command_text,server_id) VALUES (?, ?, ?)",(message.author.id, message.content,message.guild.id))
    conn.commit()
    await message.delete()
      
   
  await client.process_commands(message)


client.run(token_1.Token)
