import nextcord
from nextcord.ext import commands
from nextcord import SlashOption,Member
from typing import Optional

typew = ["panda","fox","dog","cat","bird"]
overlay_type = ["Comrade","Gay","Wasted","Jail","Mission Passed","Triggered","Wasted"]
intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = "w!",intents=intents)

@client.slash_command(name= "overlay",description="hello world")
async def overlay(interaction: nextcord.Interaction,overlay = SlashOption(required=True,description="Overlay type",choices=overlay_type),member:Optional[Member] = SlashOption(required=True,description="Member you want to put overlay on he/she")):
        link = member.avatar
        w = None
        if overlay == "Comrade":
            w = 'comrade'
        elif overlay == "Gay":
            w = 'gay'
        elif overlay == "Wasted":
            w = 'glass'
        elif overlay == "Jail":
            w = 'jail'
        elif overlay == "Mission Passed":
            w = 'passed'
        elif overlay == "Triggered":
            w = 'triggered'
        elif overlay == "Wasted":
            w = 'wasted'
        URL = f'https://some-random-api.ml/canvas/{w}?avatar={link}'
        embed = nextcord.Embed(title=f"{member.name}")
        embed.set_image(url=URL)
        await interaction.response.send_message(embed=embed)

client.run(' ')