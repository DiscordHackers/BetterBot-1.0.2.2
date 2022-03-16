from datetime import datetime
import disnake as discord
from disnake.ext import commands
from configs.config import *
from api.server import base, main


class OnGuildJoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):


        if glogs == 'true':
            serverid = guild.id
            servername = guild.name

            channel = self.client.get_channel(guildlogs)
            embed = discord.Embed(title = '🟢 Бот был добавлен на сервер!', description = f' ', color = 0x56ff2b)
            embed.add_field(name = '`Название сервера:`', value = guild.name, inline=False)
            embed.add_field(name = '`ID сервера:`', value = guild.id, inline=False)
            embed.add_field(name = '`Участников на сервере:`', value = len(guild.members), inline = False)
            embed.add_field(name = '`Регион сервера:`', value = guild.region, inline=False)
            embed.add_field(name = '`Серверов у бота:`', value = len(self.client.guilds), inline = False)
            await channel.send(embed = embed)
            await self.client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f"за {len(self.client.guilds)} серверами"))

            for member in guild.members:
                if not member.bot:
                    try:
                        # * Включение логов в канал замедляет запись
                        serverid = member.guild.id
                        servername = member.guild.name
                        channell = self.client.get_channel(bdlogs)
                        if base.user(member) is None:
                            base.send(f"INSERT INTO users VALUES ('{guild.id}', '{member}', {member.id}, 0, 0, 0, 0, 0, NULL, 0)")
                            #await channell.send(embed = main.embed(f'Был зарегестрирован пользователь {member.mention}. ID сервера: `{serverid}`. Название сервера: `{servername}`. Путем ивента on_guild_join'))                                             
                            if base.bages(member) is None:
                                base.send(f"INSERT INTO bages VALUES ('{member.name}', '{member.id}', 0, 0, 0, 0, 0, 0, 0)")
                        else:
                            pass
                    except:
                        continue

            if base.guild(guild) is None:
                base.send(f"INSERT INTO guilds VALUES ('{guild.id}', '{guild.name}', '{prefix}', '{lang}', '{currency}', NULL, NULL, NULL, NULL, NULL, 3, 'mute')")
            else:
                pass
        else:
            print("GLOGS выключены")
            for member in guild.members:
                if not member.bot:
                    try:
                        # * Включение логов в канал замедляет запись
                        serverid = member.guild.id
                        servername = member.guild.name
                        channell = self.client.get_channel(bdlogs)
                        if base.user(member) is None:
                            base.send(f"INSERT INTO users VALUES ('{guild.id}', '{member}', {member.id}, 0, 0, 0, 0, 0, NULL, 0)")
                            #await channell.send(embed = main.embed(f'Был зарегестрирован пользователь {member.mention}. ID сервера: `{serverid}`. Название сервера: `{servername}`. Путем ивента on_guild_join'))                                             
                            if base.bages(member) is None:
                                base.send(f"INSERT INTO bages VALUES ('{member.name}', '{member.id}', 0, 0, 0, 0, 0, 0, 0)")
                        else:
                            pass
                    except:
                        continue

            if base.guild(guild) is None:
                base.send(f"INSERT INTO guilds VALUES ('{guild.id}', '{guild.name}', '{prefix}', '{lang}', '{currency}', NULL, NULL, NULL, NULL, NULL, 3, 'mute')")
            else:
                pass

def setup(client):
    client.add_cog(OnGuildJoin(client))