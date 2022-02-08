import discord
import os
import requests
import json
from keep_alive import keep_alive
from listcheck import catiddict

apibaby = os.environ['apikey']
babysfirstsecret = os.environ['passkey']


client = discord.Client()

def get_cat():
  try:
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    json_data = response.json()
    newDict = json_data[0]
    catpic = newDict["url"]

    return catpic
  except Exception:
      return "Sorry! Catbot is down right now. I'm working on fixing it"


def get_cat_specfic(breed):
  try:
    catid = catiddict[breed]
    

    response = requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=" + catid)
    json_data = response.json()
    newDict = json_data[0]
    catpic = newDict["url"]
    
    return catpic
  except Exception:
      return "Sorry! Catbot was unable to perform this task. Please make sure your message was formatted correctly"

@client.event
async def on_ready():
  print("This is a test for {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("!catplease") or message.content.startswith("!cat"):
    cat = get_cat()
    await message.channel.send(cat)

  if message.content.startswith("!ihatecats"):
    await message.channel.send("What is wrong with you " + str(message.author) + "?")

  if message.content.startswith("!thiscat"):
    store = message.content.split("= ")
    breedo = store[1].lower()
    cat = get_cat_specfic(breedo)
    await message.channel.send(cat)

  if message.content.startswith("!listcats"):
    await message.channel.send(catiddict.keys())

  if message.content.startswith("!invite"):
    await message.channel.send("https://discord.com/oauth2/authorize?client_id=935951137432027299&permissions=431644735552&scope=bot")
  
  if message.content.startswith("!ping"):
    lat= round((client.latency * 1000), 2)
    await message.channel.send(str(lat) + "ms")

  if message.content.startswith("!beammeup"):
    await message.channel.send("https://i.imgur.com/b4vsFJs.png")
    
  if message.content.startswith("!help"):
    await message.channel.send("To receive a random cat, type !catplease \n" + "To get a specific breed of cat, type \n" + "!thiscatplease = *yourcatbreedhere* \n" + "To get a list of all breeds type !listcats \n"+ "Type !invite to get the invite link for this bot \n" + "Type !ping to get latency \n" + "Regular Maintenance is performed Tuesdays 9am-12pm PST \n" "This bot is operated by ya boi Blondie#4052")

  if message.content.startswith("!servers"):
    guilds = await client.fetch_guilds(limit=150).flatten()
    await message.channel.send(guilds)



keep_alive()
client.run(babysfirstsecret)
