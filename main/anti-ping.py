import nextcord 
from nextcord import Message
from nextcord.ext import commands
from nextcord.utils import get
import humanfriendly
from datetime import timedelta
import asyncio
import aiosqlite
import os

intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = "w!",intents=intents)

whitelist =  810439389883793458#-----replace this with member id // if more than one pp add [] like : whitelist = [123456789,987654123,544865464,122458555]

@client.event
async def on_ready():
    print(f"Bot is ready! maybe?")
    client.db = await aiosqlite.connect('warns.db')
    await asyncio.sleep(3)
    async with client.db.cursor() as cursor:
        await cursor.execute("CREATE TABLE IF NOT EXISTS warns(user INTEGER,guild INTEGER)")
    await client.db.commit()

async def addwarn(ctx,user):
    async with client.db.cursor() as cursor:
        await cursor.execute("INSERT INTO warns(user,guild) VALUES(?,?)",(user,ctx.guild.id))
    await client.db.commit()

async def removewarn(member):
    async with client.db.cursor() as cursor:
        await cursor.execute('SELECT * FROM warns WHERE user = ? AND guild = ?',(member.id,member.guild.id))
        data = await cursor.fetchone()
        if data:
            await cursor.execute('DELETE FROM warns WHERE user = ? AND guild = ?',(member.id,member.guild.id))

@client.event
async def on_message(message: Message):
    channel_log = client.get_channel(966189005370720267)#------ replace this with channel id
    duration = '1d' #------ how long it take?
    time = humanfriendly.parse_timespan(duration)
    if message.content == "<@810439389883793458>":
        if message.author.id != whitelist:
            async with client.db.cursor() as cursor:
                await cursor.execute('SELECT * FROM warns WHERE user = ? AND guild = ?',(message.author.id,message.author.guild.id))
                data = await cursor.fetchall()
                if data:
                    embed = nextcord.Embed(title="⚠ PING ALERT",description=f"{message.author.name}#{message.author.discriminator} has been timeout!\nduration: 1 day") #----- normal channel log?, L grammar
                    embed_log = nextcord.Embed(title="⚠ PING ALERT",description=f"{message.author.name}#{message.author.discriminator} has been timeout!\nduration: 1 day") #----- mod log,L grammar"""
                    await message.author.edit(timeout=nextcord.utils.utcnow()+timedelta(seconds=time))
                    await message.channel.send(embed=embed)
                    await removewarn(message.author)
                    await channel_log.send(embed=embed_log)
                else:
                    await addwarn(message,message.author.id)
                    await message.channel.send(f"Warned {message.author.name}")

client.run('')