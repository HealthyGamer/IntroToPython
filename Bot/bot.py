# bot.py
import os

import interactions
from dotenv import load_dotenv
from pprint import pprint

from game import Game

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('GUILD_ID'))

client = interactions.Client(token=TOKEN)

game = Game()


@client.event
async def on_ready():
    print(f'Client has connected to Discord!')


@client.command(
    name="getstats",
    description="Get your player stats",
    scope=GUILD,
)
async def get_stats(ctx: interactions.CommandContext):
    player = game.getPlayer(ctx.member.id)
    await ctx.send(f"""{ctx.member.user.username}, here are your player stats!

    Attack: {player.attack}
    HP: {player.hp}
    XP: {player.xp}
    """)

client.start()
