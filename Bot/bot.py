# bot.py
import os

import interactions
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('GUILD_ID'))

client = interactions.Client(token=TOKEN)


@client.event
async def on_ready():
    print(f'Client has connected to Discord!')


@client.command(
    name="getstats",
    description="Get your player stats",
    scope=GUILD,
)
async def get_stats(ctx: interactions.CommandContext):
    await ctx.send("Here are your player stats!")

client.start()
