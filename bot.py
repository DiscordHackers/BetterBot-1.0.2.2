import disnake as discord
import json
import os
import datetime
import asyncio
import sqlite3
from disnake.ext import commands
from disnake.ext.commands import bot, check, MissingPermissions, has_permissions
from disnake.utils import get
from os import listdir

from api.server.dataIO import fileIO
from api.check import block, support, utils
from api.server import base, main
from configs.config import *

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.guilds = True
intents.messages = True

async def get_prefix(client, message):
    connection = sqlite3.connect('data/db/main/Database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM guilds WHERE guild = {message.guild.id}")
    result = cursor.fetchone()
    return result[2]

client = commands.Bot(command_prefix = get_prefix, intents=discord.Intents.all())

client.remove_command("help")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

for filename in listdir('./commands/'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')
    else:
        if (filename != '__pycache__'):
            for file in listdir(f'./commands/{filename}/'):
                if file.endswith('.py'):
                    client.load_extension(f'commands.{filename}.{file[:-3]}')

for filename in os.listdir('./events/'):
    if filename.endswith('.py'):
        client.load_extension(f'events.{filename[:-3]}')

for filename in os.listdir('./logs/'):
    if filename.endswith('.py'):
        client.load_extension(f'logs.{filename[:-3]}')

# --------------------
# | BOT DEV CATEGORY |
# --------------------

@client.command()
@utils.developer()
async def discc(ctx, member: discord.Member):
    await member.move_to(None)
    await ctx.message.delete()
    await asyncio.sleep(3)
    await ctx.channel.purge(limit=5)

@client.event
async def on_command(command):
	info = fileIO("data/db/stats.json", "load")
	info["Commands_used"] = info["Commands_used"] + 1
	fileIO("data/db/stats.json", "save", info)

@client.command()
@block.block()
@utils.developer()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Модуль `{extension}` был загружен"))

@client.command()
@block.block()
@utils.developer()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Модуль `{extension}` был отключен"))

@client.command()
@block.block()
@utils.developer()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Модуль `{extension}` был перезагружен"))
    
@client.command()
@block.block()
@utils.developer()
async def cload(ctx, extension):
    client.load_extension(f"commands.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Команда `{extension}` была включена"))


@client.command()
@block.block()
@utils.developer()
async def cunload(ctx, extension):
    client.unload_extension(f"commands.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Команда `{extension}` была отключена"))


@client.command()
@block.block()
@utils.developer()
async def creload(ctx, extension):
    client.reload_extension(f"commands.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Команда `{extension}` была перезагружена"))


@client.command()
@block.block()
@utils.developer()
async def eload(ctx, extension):
    client.load_extension(f"events.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Событие `{extension}` было включено"))

@client.command()
@block.block()
@utils.developer()
async def eunload(ctx, extension):
    client.unload_extension(f"events.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Событие `{extension}` было отключено"))

@client.command()
@block.block()
@utils.developer()
async def ereload(ctx, extension):
    client.reload_extension(f"events.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Событие `{extension}` было перезагружено"))

@client.command()
@block.block()
@utils.developer()
async def lload(ctx, extension):
    client.load_extension(f"logs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Лог `{extension}` был загружен"))

@client.command()
@block.block()
@utils.developer()
async def lunload(ctx, extension):
    client.unload_extension(f"logs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Лог `{extension}` был отключен"))


@client.command()
@block.block()
@utils.developer()
async def lreload(ctx, extension):
    client.reload_extension(f"logs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Лог `{extension}` был  перезагружен"))
    
@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == 946486319847198816:
            ch = client.get_channel(946486319847198813)
            await ch.send("<@&946486319079632952>")
            await ch.send(embed = discord.Embed(title = 'Предупреждение', description=f'{member.mention} присоеденился к каналу <#946486319847198816>', color = 0xd57aee))
            print(f"LOGS | ВЕРИФИКАЦИЯ 1 {member.name} ({member.id})")
        elif after.channel.id == 946486319847198817:
            ch = client.get_channel(946486319847198813)
            await ch.send("<@&946486319079632952>")
            await ch.send(embed = discord.Embed(title = 'Предупреждение', description=f'{member.mention} присоеденился к каналу <#946486319847198817>', color = 0xD57AEE))
            print(f"LOGS | ВЕРИФИКАЦИЯ 2 {member.name} ({member.id})")
        elif after.channel.id == 946486319847198818:
            ch = client.get_channel(946486319847198813)
            await ch.send("<@&946486319079632952>")
            await ch.send(embed = discord.Embed(title = 'Предупреждение', description=f'{member.mention} присоеденился к каналу <#946486319847198818>', color = 0xD57AEE))
            print(f"LOGS | ВЕРИФИКАЦИЯ 3 {member.name} ({member.id})")
        elif after.channel.id == 946486319847198819:
            ch = client.get_channel(946486319847198813)
            await ch.send("<@&946486319079632952>")
            await ch.send(embed = discord.Embed(title = 'Предупреждение', description=f'{member.mention} присоеденился к каналу <#946486319847198819>', color = 0xD57AEE))
            print(f"LOGS | ВЕРИФИКАЦИЯ 4 {member.name} ({member.id})")
        elif after.channel.id == 946486320333729822:
            ch = client.get_channel(946486319847198813)
            await ch.send("<@&946486319079632952>")
            await ch.send(embed = discord.Embed(title = 'Предупреждение', description=f'{member.mention} присоеденился к каналу <#946486320333729822>', color = 0xD57AEE))
            print(f"LOGS | ВЕРИФИКАЦИЯ 5 {member.name} ({member.id})")

    
client.run(token)