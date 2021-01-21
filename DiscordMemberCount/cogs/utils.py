import discord
from discord.ext import commands

class utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    class data():
        def __init__(self, channel, channelID, count, name):
            self.channel = channel
            self.count = count
            self.name = name

    @commands.command()
    async def setup(self, ctx, channelName):
          if ctx.message.author.guild_permissions.administrator:
                self.data.count = ctx.guild.member_count
                self.data.name = channelName
                self.data.channel = await ctx.guild.create_voice_channel(f"{self.data.name} : {self.data.count}")
    
    @commands.command()
    async def update(self, ctx):
         if ctx.message.author.guild_permissions.administrator:
                self.data.count = ctx.guild.member_count
                await self.data.channel.edit(name = f"{self.data.name} : {self.data.count}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.data.count = self.data.count + 1
        await self.data.channel.edit(name = f"{self.data.name} : {self.data.count}")
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        self.data.count = self.data.count - 1
        await self.data.channel.edit(name = f"{self.data.name} : {self.data.count}")

def setup(client):
    client.add_cog(utils(client))