import asyncio, discord, sys, os, io
#Encoding error solved
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

from discord.ext import commands
import requests
from bs4 import BeautifulSoup

#crawler
url = 'https://www.op.gg/champion/statistics'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')



#token path
token_path = os.path.dirname(os.path.abspath(__file__)) + "/token.txt"
t = open(token_path,"r",encoding="utf-8")
token = t.read().split()[0]

#bot prefix set
bot = commands.Bot(command_prefix='!')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(token)

#client.run('NzEzODI5ODk3NjAwMTA2NTc3.Xsl0DA.sLqw8o_855BJ5O2UGDFU8wvhOoI')
