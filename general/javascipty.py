import discord
import os
import praw
from asyncio import sleep
from random import randint
from discord.ext import commands, tasks
from discord.utils import get

client = commands.Bot(command_prefix='.', description='r/javascipty (private)')
TOKEN = os.getenv('TOKEN')
SECRET = os.getenv('SECRET')
ID = os.getenv('ID')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

reddit = praw.Reddit(user_agent="Post Grabber? (/u/javascipty)",
                     client_secret=SECRET,
                     client_id=ID,
                     username=USERNAME,
                     password=PASSWORD,
                     check_for_async=False
                     )

@client.event
async def on_ready():
    print(f'Started {client.user}')
    await client.change_presence(status=discord.Status.dnd)

async def new():
    guild = client.get_guild(864693306570702878)
    channel = guild.get_channel(864693307186610239)
    message = await channel.fetch_message(channel.last_message_id)
    option = randint(1, 4)
    print(option)
    if option == 1:
        posts = reddit.subreddit("javascipty").hot(limit=1000)
    elif option == 2:
        posts = reddit.subreddit("javascipty").new(limit=1000)
    elif option == 3:
        posts = reddit.subreddit("javascipty").top(limit=1000)
    elif option == 4:
        posts = reddit.subreddit("javascipty").rising(limit=1000)
    for post in posts:
        num = randint(1, 1000)
        num2 = randint(1, 100)
        if num % num2 == 0:
            embed = discord.Embed(title='', color=discord.Color(0xe8d8df))
            embed.set_image(url=post.url)
            await message.edit(embed=embed)
            break

@tasks.loop(seconds=3)
async def loop_restart():
    await new()

@loop_restart.before_loop
async def before_loop_restart():
    print('waiting...')
    await client.wait_until_ready()

loop_restart.start()
if __name__ == '__main__':
    client.run(TOKEN, reconnect=True)