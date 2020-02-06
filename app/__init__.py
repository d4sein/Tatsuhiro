from discord.ext import commands

import config


TOKEN = config.TOKEN
client = commands.Bot(command_prefix=';')
