import nextcord 
from nextcord import Message
from nextcord.ext import commands
import humanfriendly
from datetime import timedelta

intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = "w!",intents=intents)
whitelist =  810439389883793458#-----replace this with member id // if more than one pp add [] like : whitelist = [123456789,987654123,544865464,122458555]

@client.event
async def on_ready():
    print(f"Bot is ready! maybe?")

@client.event
async def on_message(message: Message):
    channel_log = client.get_channel(966189005370720267)#------ replace this with channel id
    duration = '1d' #------ how long it take?
    time = humanfriendly.parse_timespan(duration)
    if message.content.startswith("https://discord.gg/"):
        if message.author.id != whitelist:
            em_log = nextcord.Embed(title="⚠ INVITE LINK ALERT",description=f"{message.author.name}#{message.author.discriminator} has been timeout!\nduration: 1 day")
            em = nextcord.Embed(title="⚠ INVITE LINK ALERT",description=f"{message.author.name}#{message.author.discriminator} has been timeout!\nduration: 1 day")
            await message.channel.purge(limit=1)
            await message.author.edit(timeout=nextcord.utils.utcnow()+timedelta(seconds=time))
            await message.channel.send(embed = em)
            await channel_log.send(embed=em_log)

client.run(' ')