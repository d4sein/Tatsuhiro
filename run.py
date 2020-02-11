from pathlib import Path
import json

import discord

from app import client
from config import TOKEN, COG_DIR


with open('config.json', 'r') as f:
    config = json.load(f)


@client.event
async def on_ready():
    await client.change_presence(
        status=config['status'],
        activity=discord.Game(config['activity']))

    print('Up and running!')


def load_extensions(cogs: str) -> None:
    '''
    Loads all extensions recursively

    Params:
        cogs: str
        Relative path to cogs dir
    '''

    for extension in Path(cogs).rglob('*.py'):
        extension = '.'.join(extension.parts)[:-3]

        try:
            client.load_extension(extension)
            print(f'{extension} has been loaded.')
        except Exception as e:
            print(f'{extension} could not be loaded: {e}')


if __name__ == '__main__':
    load_extensions(COG_DIR)
    client.run(TOKEN)
