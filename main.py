import os
import __main__
from dotenv import load_dotenv

import discord
from model_discord import Model, getPrediction
from reponse_discord import getAnswer

setattr(__main__, "Model", Model)
load_dotenv()

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We are logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.bot:
        return
    msg = str(message.content)
    predictions = getPrediction(msg)
    await getAnswer(predictions, message)


client.run(os.getenv('discord_bot_env'))

