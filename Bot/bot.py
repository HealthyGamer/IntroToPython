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
    player = game.getPlayer(str(ctx.member.id))
    await ctx.send(f"""{ctx.member.user.username}, here are your player stats!

    Id: {player.id}
    Attack: {player.attack}
    HP: {player.current_hp}
    XP: {player.xp}
    Game: Players: {len(game.players)} Encounters: {len(game.encounters)}
    """)


@client.command(
    name="encounter",
    description="Create a new encounter",
    scope=GUILD,
)
async def create_encounter(ctx: interactions.CommandContext):
    result = game.createEncounter(str(ctx.member.id))
    await ctx.send(result)


@client.command(
    name="attack",
    description="Attack!!!!!!",
    scope=GUILD,
)
async def player_action(ctx: interactions.CommandContext):
    result = game.playerAction(str(ctx.member.id))
    await ctx.send(result)


@client.command(
    name="run",
    description="Run away",
    scope=GUILD,
)
async def complete_encounter(ctx: interactions.CommandContext):
    result = game.completeEncounter(str(ctx.member.id))
    await ctx.send(result)


client.start()
