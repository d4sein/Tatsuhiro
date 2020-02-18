import discord
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['expulsar'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason: str = None) -> None:
        if member is None:
            await ctx.send('Você esqueceu do argumento `<@usuário>`.')
            return

        try:
            await member.ban(reason=reason)
        except Exception as e:
            print(f'Could not kick the user "{member}": ', e)
            ctx.send('Não consegui expulsar esse usuário.')
        else:
            ctx.send('Usuário expulso!')
        finally:
            return


def help():
    return {
        'name': 'Expulsar',
        'usage': 'expulsar <@usuário> [motivo]',
        'aliases': 'kick',
        'description': 'Expulsa o usuário do servidor'
    }


def setup(client):
    client.add_cog(Kick(client))
