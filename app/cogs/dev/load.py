import discord
from discord.ext import commands


class Load(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension: str=None) -> None:
        try:
            self.client.load_extension(extension)
        except Exception as e:
            print(f'{extension} could not be loaded: {e}')
        else:
            print(f'{extension} has been loaded.')


def help():
    return {
        'name': 'Load',
        'usage': 'load <extension>',
        'description': 'Loads an extension'
    }


def setup(client):
    client.add_cog(Load(client))
