import os # to get the token for bot
import discord #discord function
from keep_alive import keep_alive
import random
from discord.utils import find
from member_class import discordUser
from replit import db
import json
import ast
from time import sleep

intent = discord.Intents.default()
intent.message_content = True
intent.presences = True
intent.messages = True

client = discord.Client(intents=intent)

command = False
helpmsg = 'Here is a list of commands for you losers to use. (Version 1)\n\n1. /bmbot adduser {name_to_be_used} {ping the person}\nExplanation: This creates an account for the user so mentions can be stored.\n\n2. /bmbot addmentionmsg {name_to_be_used} {msg}\nExplanation: Adds the mention msg when the user is pinged\n\n3. /bmbot listmentionmsg {name_of_user} \nExplanation: This lists all the possible mention messages the account has.\n\n4. /bmbot deletementionmsg {name} {position}\nExplanation:Deletes a mention message, refer to listing to decide which mention to remove. 

def addDiscordUser(id,name):
  if id not in db.keys():
    db[id] = json.dumps(discordUser(name).toJson())
    msg = "{0} is now added!".format(name)
  else:
    msg = "The user {0} has already been added!".format(name)
  return msg

def get_id(name):
  for i in db.keys():
    value = ast.literal_eval(json.loads(db[i]))
    if value['name'] == name:
      return i
      

def add_mentionsMsg(id, mentionMsg):
  if id in db.keys():
    user = ast.literal_eval(json.loads(db[id]))
    user['mentionList'].append(mentionMsg)
    db[id] = json.dumps(str(user))
    msg = 'Mention message has been added!'
  else:
    msg = 'The user cannot be found.'
  return msg
    
def delete_mentionsMsg(id,position):
  if id in db.keys():
    user = ast.literal_eval(json.loads(db[id]))
    if len(user['mentionList']) > position-1:
      user['mentionList'].pop(position-1)
      db[id] = json.dumps(str(user))
      msg = 'Mention msg has been deleted as per your shitty taste, enjoy!'
    else:
      msg = 'Position chosen does not exist'
  else:
    msg = "The user cannot be found, try typing a name that exist."

  return msg

def returnMentionMsg(user):
  dictStuff = ast.literal_eval(json.loads(user))
  msg = random.choice(dictStuff['mentionList'])
  return msg

def listallmention(user):
  dictStuff = ast.literal_eval(json.loads(db[user]))
  list = (dictStuff['mentionList'])
  msg = ''
  for i in range(0,len(list)):
    msg += '{0}. {1}\n'.format(i+1,list[i])
  return msg

@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}'.format(guild.name)+ ' people! I am totally not a bot created by a certain orphan :)')


@client.event
async def on_ready():
  print('A tax evader known as {0.user}'.format(client) +' has entered through a portal.')
  


@client.event
async def on_message(message): #check if the msg is sent by the bot itself
  if message.author == client.user:
    return

  if client.user.mentioned_in(message):
    await message.channel.send('Leave me alone, I\'m watching loli hentai.')
  
  if message.content.startswith('/bmbot'): 
    command = True
    msg = message.content.split()
    if msg[1] == 'adduser':
      msg = addDiscordUser(msg[3][2:20], msg[2])

    if msg[1] == 'addmentionmsg':
      stringMsg = " ".join(msg[3:])
      id = get_id(msg[2])
      msg = add_mentionsMsg(id,stringMsg)

    if msg[1] == 'deletementionmsg':
      id = get_id(msg[2])
      msg = delete_mentionsMsg(id,int(msg[3]))
      
    if msg[1] == 'listmentionmsg':
      id = get_id(msg[2])
      msg = listallmention(id)
    if msg[1] == 'help':
      msg = helpmsg
      
    await message.channel.send(msg)

  else:
    command = False
    
  if (len(message.mentions)>0 and command==False): #if there was a mention in message
    for i in range(0,len(message.mentions)):
      if str(message.mentions[i].id) in db.keys():
        await message.channel.send(returnMentionMsg(db[str(message.mentions[i].id)]))
      


while __name__ == '__main__':
  try:
    keep_alive()
    client.run(os.environ['token'])
  except discord.errors.HTTPException as e:
    print(e)
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    sleep(7)
    os.system('kill 1')

