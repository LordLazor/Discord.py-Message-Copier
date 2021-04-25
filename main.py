import discord
from discord.ext import commands
import asyncio

TOKEN = 'ODMxOTI1MjA1NTc5MzMzNzIy.YHcUuQ._f9MLXtkR9MjA3mWwyRQ1tbNCug'

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print("Ready")
    while True:
        await bot.change_presence(status=discord.Status.idle,
                                  activity=discord.Activity(type=discord.ActivityType.listening,
                                                            name="Copying messages"))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.idle,
                                  activity=discord.Game(name="created by Lazar"))
        await asyncio.sleep(10)
bot.grabbed = 1
@bot.command()
async def grab(ctx, amount = 20):
    await ctx.message.delete()
    await ctx.send(f'Grabbing the last **{amount}** messages in **{ctx.channel.name}**.')
    message = await ctx.send(f'Grabbed {bot.grabbed} messages.')
    filename = f"{ctx.channel.name}.txt"
    with open(filename, "w") as file:
        async for msg in ctx.channel.history(limit=amount):
            if not ctx.author.bot:
                file.write(f"{msg.created_at} - {msg.author.display_name}: \n{msg.content}\n\n")
                bot.grabbed += 1
                await message.edit(content=f'Grabbed {bot.grabbed} messages.')
    await ctx.send('Finished...')

bot.run(TOKEN, bot=True)