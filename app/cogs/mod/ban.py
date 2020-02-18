import discord
from discord.ext import commands


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['banir'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason: str = None) -> None:
        if member is None:
            await ctx.send('Você esqueceu do argumento `<@usuário>`.')
            return

        try:
            await member.ban(reason=reason)
        except Exception as e:
            print(f'Could not ban the user "{member}": ', e)
            ctx.send('Não consegui banir esse usuário.')
        else:
            ctx.send('Usuário banido!')
        finally:
            return


def help():
    return {
        'name': 'Ban',
        'usage': 'ban <@usuário> [motivo]',
        'description': 'Bane o usuário do servidor'
    }


def setup(client):
    client.add_cog(Ban(client))
