import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix= "m!", intents=intents)

@client.command()
@commands.is_owner()
async def load (ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send("> cog loaded")

@client.command()
@commands.is_owner()
async def unload (ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send("> cog unloaded")

@client.command()
@commands.is_owner()
async def reload (ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send("> cog reloaded")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')
        
client.run("ODAxNzM3MDAwMjMxMjM5NzAx.YAlBxA.y8eUkFmZDL4Pds-_KwspIOai8RE")