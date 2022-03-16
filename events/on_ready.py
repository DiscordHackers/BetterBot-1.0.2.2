from datetime import datetime
import disnake as discord
import random
from disnake.ext import commands, tasks
from configs.config import *
from api.server import base, main
import psutil
import datetime, time

class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        #await self.client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f"help | client"))
        print("ptero start") # [[ Для того чтобы птеродактиль определил что сервер прошел инициализацию и уже запущен ]] #
        print("Успешно подключился к серверам Discord")
        print(f'Имя: {self.client.user.name}')
        print(f'ID: {self.client.user.id}')
        global startTime
        startTime = time.time()        
        #self.status_task.start()

        for guild in self.client.guilds:
            print(guild.id , guild.name)

        if vchange == 'true':
            channel = self.client.get_channel(versionid)
            await channel.edit(name = f'{versionname}: {version}')
        else:
            print("Отключена функция 1")

        for guild in self.client.guilds:
            if base.guild(guild) is None:
                base.send(f"INSERT INTO guilds VALUES ('{guild.id}', '{guild.name}', '{prefix}', '{lang}', '{currency}', NULL, NULL, NULL, NULL, NULL, 3, 'mute')")
            else:
                pass
            
            if blogs == 'true':
                for member in guild.members:
                    if not member.bot:
                        try:
                            serverid = member.guild.id
                            servername = member.guild.name
                            channell = self.client.get_channel(bdlogs)
                            if base.user(member) is None:	
                                base.send(f"INSERT INTO users VALUES ('{guild.id}', '{member}', '{member.id}', 0, 0, 0, 0, 0, NULL, 0)")
                                await channell.send(embed = main.embed(f'Был зарегестрирован пользователь {member.mention}. ID сервера: `{serverid}`. Название сервера: `{servername}`. Путем ивента on_ready'))
                                if base.bages(member) is None:
                                    base.send(f"INSERT INTO bages VALUES ('{member.name}', '{member.id}', 0, 0, 0, 0, 0, 0, 0)")                          
                            else:
                                pass
                        except:
                            continue
            else:
                for member in guild.members:
                    if not member.bot:
                        try:
                            serverid = member.guild.id
                            servername = member.guild.name
                            channell = self.client.get_channel(bdlogs)
                            if base.user(member) is None:	
                                base.send(f"INSERT INTO users VALUES ('{guild.id}', '{member}', '{member.id}', 0, 0, 0, 0, 0, NULL, 0)")
                                if base.bages(member) is None:
                                    base.send(f"INSERT INTO bages VALUES ('{member.name}', '{member.id}', 0, 0, 0, 0, 0, 0, 0)")                          
                            else:
                                pass
                        except:
                            continue


    @commands.command(name='stats')
    async def _stats(self,ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        memory = psutil.virtual_memory().total / (1024.0 ** 3)
        await ctx.send(embed = discord.Embed(title = 'Информация', description = f'``` • Пинг          :: {round(self.client.latency * 1000)} \n • ОЗУ исп.      :: {round(memory)} MB \n • Аптайм бота   :: {uptime} \n\n • disnake       :: v{discord.__version__} \n • Версия бота   :: {version} ```'))                                                 

    #@tasks.loop(minutes = 0.2)
    #async def status_task(self):
        #await self.client.change_presence(activity = discord.Game(random.choice(status)))

def setup(client):
    client.add_cog(OnReady(client))