import discord
from discord.ext import commands


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=None) -> None:
        if amount is None:
            await ctx.send('Missing `<amount>` argument.')
            return

        try:
            amount = int(amount)
        except ValueError:
            await ctx.send('`<amount>` must be of type "int".')
            return

        if amount <= 0 or amount >= 100:
            await ctx.send('`<amount>` must be in {1...99}.')
            return

        messages = []

        async for message in ctx.channel.history(limit=amount+1):
            messages.append(message)

        await ctx.channel.delete_messages(messages)


def help():
    return {
        'name': 'Clear',
        'usage': 'clear <amount>',
        'description': 'Bulk deletes messages from a channel'
    }


def setup(client):
    client.add_cog(Clear(client))
