import discord
from discord.ext import commands
import subprocess


intents = discord.Intents.default()
intents.typing = False  # Disable typing notifications
intents.messages = True  # Enable GUILD_MESSAGES intent
intents.presences = False  # Disable presences
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Define a command to trigger execution of the local Python script
@bot.command()
async def server_downtime(ctx):
    # Call the local Python script using subprocess
    await ctx.send("Wait a bit im working on it! :)")
    subprocess.run(["python", "main.py"])
    await ctx.send("Generated by Khealim's osrs crawler!")

# Run the bot with your Discord bot token
bot.run('')