import discord
from discord.ext import commands

from app import config


class Ask(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['perguntar'])
    async def ask(self, ctx) -> None:
        try:
            color = int(config['EMBED']['COLOR'])
        except ValueError as e:
            print('Could not type cast color from str to int: ', e)
            return

        description = '''
        1. Pesquise antes de perguntar
        2. Descreva seu problema com detalhes o quanto for necessário
        3. Mande o código fonte ou repositório para reprodução
        '''

        embed = discord.Embed(
            title = 'Como fazer uma pergunta:',
            description = description,
            color = discord

            .Color(color)
        )

        await ctx.send(embed=embed)


def help():
    return {
        'name': 'Ask',
        'usage': 'pergunta',
        'aliases': 'ask',
        'description': 'Manda instruções de como fazer uma pergunta produtiva'
    }


def setup(client):
    client.add_cog(Ask(client))
