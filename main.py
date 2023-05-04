import poe
import logging
import sys
import os
import json

#Bots:
#{'capybara': 'Sage', 
# 'beaver': 'GPT-4', #1 msg limit for free accounts
# 'a2_2': 'Claude+', #3 msg limit for free accounts
# 'a2': 'Claude-instant',
# 'chinchilla': 'ChatGPT',
# 'hutia': 'NeevaAI',
# 'nutria': 'Dragonfly'}
print("Commands enterable in the \"Enter prompt\" field:\n/clear -- Clears context\n/changebot -- Runs the change bot function\n/purge -- Deletes all conversation history")

try:
  token = os.environ['token']
except NameError:
  token = input("\nEnter token: ")
except KeyError:
  token = input("\nEnter token: ")
else:
  print("\nEnvironment variable \'token\' used")

client = poe.Client(token)

currentBot = "capybara"

def changeBot():
  botnames = client.bot_names
  print(json.dumps(botnames, indent=2))
  botInput = input("\nChoose a bot\nTo do this, enter the name of the bot on the left\n(ex: capybara) for the bot that you want to use (ex: Sage)\nIf you hit enter without typing anything,\nSage will be chosen by default.\nInput: ")
  global currentBot
  if botInput == "":
    currentBot = "capybara"
  else:
    currentBot = botInput

  print("Bot chosen: " + currentBot)
  return

changeBot()

def send_message():
  message = input("\nEnter prompt: ")
  print(message)
  if message.lower() == "/clear":

    client.send_chat_break(currentBot)
    print("Context cleared for " + currentBot)
    return

  if message.lower() == "/changebot":
    changeBot()
    return

  if message.lower() == "/purge":
    client.purge_conversation(currentBot, count=32767)
    return
  
  poe.logger.setLevel(logging.INFO)
  
  for chunk in client.send_message(currentBot, message, with_chat_break=False, timeout=15):
    print(chunk["text_new"], end="", flush=True)

while True:
  send_message()