import json

from discord.ext import commands

import config


with open('config.json', 'r') as f:
    config = json.load(f)

client = commands.Bot(command_prefix=config['prefix'])
