import discord
from discord.ext import commands


class Reload(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension: str = None) -> None:
        try:
            self.client.reload_extension(extension)
        except Exception as e:
            print(f'{extension} could not be reloaded: {e}')
        else:
            print(f'{extension} has been reloaded.')


def help():
    return {
        'name': 'Reload',
        'usage': 'reload <extension>',
        'description': 'Reloads an extension'
    }


def setup(client):
    client.add_cog(Reload(client))
