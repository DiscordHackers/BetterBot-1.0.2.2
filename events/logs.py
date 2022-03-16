from datetime import datetime
import disnake
from disnake.ext import commands
from configs.config import *

class logs(commands.Cog):
    def __init__(self, client):
        self.client = client

   #ON MEMEBR JOIN

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if logsm == 'true':
            serverid = member.guild.id
            servername = member.guild

            with open(f"logs/mainlog/on-member-join-logs.log", "a", encoding = "utf-8") as file:
                file.write(f"[{datetime.utcnow()}]\n-=-\n🟢 Был зарегестрирован пользователь {member}. ID сервера: `{serverid}`. Название сервера: `{servername}`. Путем ивента on_member_join\n-=-\n")
        else:
            pass

    #ON MEMBER LEAVE
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if logsm == 'true':
            with open(f"logs/mainlog/on-member-remove-logs.log", "a", encoding = "utf-8") as file:
                file.write(f"[{datetime.utcnow()}]\n-=-\n🔴 Был удалён пользователь {member}. Путем ивента on_member_remove\n-=-\n")
        else:
            pass
    

    #ON GUILD JOIN
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if logsg == 'true':
            serverid = guild.id
            servername = guild.name

            with open(f"logs/mainlog/on-guild-join-logs.log", "a", encoding = "utf-8") as file:
                file.write(f"[{datetime.utcnow()}]\n-=-\n🟢 Бот был добавлен на сервер!\n`Название сервера:` {servername}\n`ID сервера:` {serverid}\n`Участников на сервере:` {len(guild.members)}\n`Серверов у бота:` {len(self.client.guilds)}\n-=-\n")
        else:
            pass


    #ON GUILD REMOVE
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        if logsg == 'true':
            serverid = guild.id
            servername = guild.name

            with open(f"logs/mainlog/on-guild-remove-logs.log", "a", encoding = "utf-8") as file:
                file.write(f"[{datetime.utcnow()}]\n-=-\n🔴 Бот был удалён с сервера!\n`Название сервера:` {servername}\n`ID сервера:` {serverid}\n`Участников на сервере:` {len(guild.members)}\n`Серверов у бота:` {len(self.client.guilds)}\n-=-\n")
        else:
            pass

    
    @commands.Cog.listener()
    async def on_message(self, message):
        if logsgc == 'true':
            with open(f"logs/mainlog/guilds/{message.guild.id}-chatlog.log", "a", encoding = "utf-8") as file:
                    file.write(f"Пользователь {message.author} написал: [ {message.content} ]\n-=--=-\n")
        else:
            pass

def setup(client):
    client.add_cog(logs(client))