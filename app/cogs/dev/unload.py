import discord
from discord.ext import commands


class Unload(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension: str=None) -> None:
        try:
            self.client.unload_extension(extension)
        except Exception as e:
            print(f'{extension} could not be unloaded: {e}')
        else:
            print(f'{extension} has been unloaded.')


def help():
    return {
        'name': 'Unload',
        'usage': 'unload <extension>',
        'description': 'Unloads an extension'
    }


def setup(client):
    client.add_cog(Unload(client))
