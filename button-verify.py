import nextcord 
from nextcord.ext import commands
from nextcord.utils import get

intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = "w!",intents=intents)

@client.event
async def on_ready():
    print(f"Bot is ready! maybe?")
    
class ButtonCreate(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label="✅ Verify", style=nextcord.ButtonStyle.blurple
    )
    async def role(self, button:nextcord.ui.Button,interaction: nextcord.Interaction):
        member = interaction.user
        role = get(member.guild.roles, name="TEST") #--------replace TEST with role name
        if role in member.roles:
            await interaction.response.send_message(content=f"You already have a role",ephemeral=True)
        else:
            await interaction.response.send_message(content=f"Gived role success",ephemeral=True)
            await member.add_roles(role,member)
            

@client.slash_command(name="setup")
async def set(interaction:nextcord.Interaction):
    await interaction.channel.send(view=ButtonCreate()) #you can add embed=??? or content=??? or anything you want ;)
    await interaction.response.send_message(content="Setup successful!",ephemeral=True)

client.run(' ')