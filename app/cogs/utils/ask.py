import discord
from discord.ext import commands

from app import config


class Ask(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ask(self, ctx) -> None:
        try:
            color = int(config['EMBED']['COLOR'])
        except ValueError as e:
            print('Could not type cast color from str to int: ', e)
            return
        
        description = '''
        1. Do your research before asking
        2. Describe your problem as detailed as needed
        3. Send the source code
        '''

        embed = discord.Embed(
            title = 'How to ask a question:',
            description = description,
            color = discord.Color(color)
        )

        await ctx.send(embed=embed)


def help():
    return {
        'name': 'Ask',
        'usage': 'ask',
        'description': 'Sends instructions on how to ask a question'
    }


def setup(client):
    client.add_cog(Ask(client))
