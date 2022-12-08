import discord
from discord import app_commands

def superchat(money):
    if(money<30 and money>=1):
        cor = discord.Color.blue()
    if(money<75 and money>=30):
        cor = discord.Color.teal()
    if(money<150 and money>=75):
        cor = discord.Color.green()
    if(money<300 and money>=150):
        cor = discord.Color.yellow()
    if(money<750 and money>=300):
        cor = discord.Color.orange()
    if(money<1500 and money>=750):
        cor = discord.Color.magenta()
    if(money>=1500):
        cor = discord.Color.red()
    return cor
