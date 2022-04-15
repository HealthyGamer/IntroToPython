from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext

class SlashCommands
  @slash.slash(name="getStats")
  async def test(ctx: SlashContext):
    embed = Embed(title="Embed Test")
    await ctx.send(embed=embed)
    
  @slash.slash(name="startCombat")
  async def test(ctx: SlashContext):
    embed = Embed(title="Embed Test")
    await ctx.send(embed=embed)
