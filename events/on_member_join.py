from datetime import datetime
import disnake as discord
from disnake.ext import commands
from disnake.utils import get
from api.server import base, main
from configs.config import *


class OnMemberJoin1(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):

        if blogs == 'true':
            if not member.bot:
                if base.guild(member.guild)[5] is not None:
                    role = get(member.guild.roles, id = base.guild(member.guild)[5])
                    await member.add_roles(role)
                else:
                    pass
                serverid = member.guild.id
                servername = member.guild.name
                channel = self.client.get_channel(bdlogs)
                if base.user(member) is None:
                    base.send(f"INSERT INTO users VALUES ('{member.guild.id}', '{member}', {member.id}, 0, 0, 0, 0, 0, NULL, 0)")
                    await channel.send(embed = main.embed(f'Был зарегестрирован пользователь {member.mention}. ID сервера: `{serverid}`. Название сервера: `{servername}`. Путем ивента on_member_join'))            
                    if base.bages(member) is None:
                        base.send(f"INSERT INTO bages VALUES ('{member.name}', '{member.id}', 0, 0, 0, 0, 0, 0, 0)")           
                else:
                    pass
        else:
            if not member.bot:
                if base.guild(member.guild)[5] is not None:
                    role = get(member.guild.roles, id = base.guild(member.guild)[5])
                    await member.add_roles(role)
                else:
                    pass
                serverid = member.guild.id
                servername = member.guild.name
                channel = self.client.get_channel(bdlogs)
                if base.user(member) is None:
                    base.send(f"INSERT INTO users VALUES ('{member.guild.id}', '{member}', {member.id}, 0, 0, 0, 0, 0, NULL, 0)")
                    if base.bages(member) is None:
                        base.send(f"INSERT INTO bages VALUES ('{member.name}', '{member.id}', 0, 0, 0, 0, 0, 0, 0)")           
                else:
                    pass            

def setup(client):
    client.add_cog(OnMemberJoin1(client))