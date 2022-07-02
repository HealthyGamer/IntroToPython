import os

import interactions
from dotenv import load_dotenv

from game import Game

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = int(os.getenv("GUILD_ID"))

client = interactions.Client(token=TOKEN)
game = Game()

@client.event
async def on_ready():
    print("Client is connected to Discord")

@client.command(
    name="getstats",
    description="Get your player stats",
    scope=GUILD
)
async def get_stats(ctx: interactions.CommandContext):
    player = game.get_player(str(ctx.member.id))
    await ctx.send(f"""{ctx.member.user.username}, here are your stats:
    
    Attack: {player.attack}
    HP: {player.hp}
    XP: {player.xp}
    """)

@client.command(
    name="encounter",
    description="Create a new encounter",
    scope=GUILD
)
async def create_encounter(ctx: interactions.CommandContext):
    encounter = game.create_encounter(str(ctx.member.id))
    await ctx.send(encounter)

@client.command(
    name="run",
    description="Run away!!!!!",
    scope=GUILD
)
async def run_away(ctx: interactions.CommandContext):
    result = game.complete_encounter(str(ctx.member.id))
    await ctx.send(result)

@client.command(
    name="attack",
    description="Attack!!!!!",
    scope=GUILD
)
async def run_away(ctx: interactions.CommandContext):
    result = game.attack(str(ctx.member.id))
    await ctx.send(result)

client.start()