import nextcord 
from nextcord.ext import commands
from nextcord.utils import get

intents = nextcord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = "w!",intents=intents)

passcode = "nah"

class Modal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            f"Passcode : {passcode}"
        )
        self.Title = nextcord.ui.TextInput(label = f"Passcode",min_length = 3,max_length =3, required = True,placeholder = "Place passcode here")
        self.add_item(self.Title)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        if self.Title.value == passcode:
            member = interaction.user
            role = get(member.guild.roles, name="TEST") #--------replace TEST with role name
            if role in member.roles:
                await interaction.response.send_message(content=f"You already have a role",ephemeral=True)
            else:
                await interaction.response.send_message(content=f"Gived role success",ephemeral=True)
                await member.add_roles(role,member)
        else:
            await interaction.response.send_message(content=f"Wrong passcode!",ephemeral=True)

@client.slash_command()
async def verify(interaction:nextcord.Interaction):
    await interaction.response.send_modal(Modal())

client.run(' ')