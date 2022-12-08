import discord
from discord import app_commands
import cod.fun

class aclinet(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}")


client = aclinet()
tree = app_commands.CommandTree(client)


@tree.command(name = "sc", description = "您的贊助金額和訊息都會公開顯示,訊息請留在chat" )
async def self(interaction: discord.Integration, money:int, foruser:str, chat:str=""):  
    channel = client.get_channel(interaction.channel.id)
    user = str(interaction.user).split('#')[0]
    cor = cod.fun.superchat(money)
    embed = discord.Embed(title=f"${money}", description=f"謝謝{user}給{foruser}的Super chat", color=cor)
    embed.set_author(name=f"{user}", icon_url='https://cdn.discordapp.com/attachments/1048644726577975296/1050296879495262259/84b82d07b293907113d9d4dafd29bfa170bbf9b6.png')
    if(chat == ""):
        chat = ""
    else:
        embed.add_field(name=f"{chat}", value=".")
    await interaction.response.send_message(money, ephemeral=True)
    print(f"from {interaction.user}(<{interaction.user.id}>)say")
    try:
        await channel.send(embed=embed)
    except:
        await channel.send("餘額不足QAQ")

@tree.command(name = "倒讚", description = "#春魚對不起")
async def self(interaction: discord.Integration, txt:str=""):
    channel = client.get_channel(interaction.channel.id)
    user = str(interaction.user).split('#')[0]
    embed = discord.Embed(title="瘋狂倒讚", description=f"{txt}")
    embed.set_author(name=f"{user}", icon_url='https://cdn.discordapp.com/attachments/1048644726577975296/1050296879495262259/84b82d07b293907113d9d4dafd29bfa170bbf9b6.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1048644726577975296/1050307386537156658/maxresdefault.jpg')
    await interaction.response.send_message("倒讚", ephemeral=True)
    print(f"from {interaction.user}(<{interaction.user.id}>)say")
    try:
        await channel.send(embed=embed)
    except:
        await channel.send("對方太棒了，你不可以倒讚")

client.run("MTA0OTkzMjY5MTkxMjUyMzg1OA.GeNmis.symeolI3ol7qmB8Fq2Kvp5KOuZZj6qDcHuPUPs")