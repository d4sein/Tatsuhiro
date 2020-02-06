import json
import os

import discord

from app import client, TOKEN
from config import COG_DIR


with open('config.json', 'r') as f:
	config = json.load(f)


@client.event
async def on_ready():
	await client.change_presence(
        status=config['status'],
        activity=discord.Game(config['activity']))

	print('Up and running!')


def load_extensions(cogs: str) -> None:
    for category in os.listdir('app/' + cogs):
        extensions = [file.replace('.py', '') for file in os.listdir(f'app/{cogs}/{category}') if file.endswith('.py')]

        for extension in extensions:
            extension_dir = f'app.{cogs}.{category}.{extension}'

            try:
                client.load_extension(extension_dir)
                print(f'{extension_dir} loaded.')
            except Exception as e:
                print(f'{extension_dir} could not be loaded: {e}')


load_extensions(COG_DIR)
client.run(TOKEN)
