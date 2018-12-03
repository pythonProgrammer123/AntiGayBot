import discord
import asyncio
import random
import time
import os





client = discord.Client()

chat_filter = ["GAY"]

@client.event
async def on_ready():
    print("-----------")
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("BOT IS READY!")
    print("------------")


@client.event
async def on_message(message):
    channel = client.get_channel("lagu_pacak")
    print(message.author.name)
    print(message.author.id)
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            await client.send_message(message.channel, "***DID SOMEONE JUST SAY GAY? LMAO YOU NIGGAS GAY!***")
            await client.send_message(message.channel, "https://imgur.com/gallery/f4jxP")
        

            
            



client.run(os.environ.get("clientToken"))


