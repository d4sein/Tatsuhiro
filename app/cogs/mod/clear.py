import discord
from discord.ext import commands


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['apagar'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=None) -> None:
        if amount is None:
            await ctx.send('Você esqueceu do argumento `<quantidade>`.')
            return

        try:
            amount = int(amount)
        except ValueError:
            await ctx.send('A quantidade precisa ser um número inteiro.')
            return

        if amount <= 0 or amount >= 100:
            await ctx.send('A quantidade precisa estar entre 0 e 100.')
            return

        messages = []

        async for message in ctx.channel.history(limit=amount+1):
            messages.append(message)

        await ctx.channel.delete_messages(messages)


def help():
    return {
        'name': 'Apagar',
        'usage': 'apagar <quantidade>',
        'aliases': 'clear',
        'description': 'Apaga mensagens em massa de um canal'
    }


def setup(client):
    client.add_cog(Clear(client))
