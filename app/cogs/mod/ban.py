import discord
from discord.ext import commands


class Ban(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member=None, *, reason: str=None) -> None:
		if member is None:
			return await ctx.send('Missing `<@user>` argument.')

		await member.ban(reason=reason)


def help():
	return {
		'name': 'Ban',
		'usage': 'ban <@user> [reason]',
		'description': 'Bans a member from the server'
	}


def setup(client):
	client.add_cog(Ban(client))
