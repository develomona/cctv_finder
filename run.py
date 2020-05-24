import asyncio, discord, sys, os, io
#Encoding error solved
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# import requests

# .lower()
champ_name = 'gragas'
location = 'jungle'

#crawler
url = 'https://www.op.gg/champion/'+champ_name+'/statistics/'+location+'/rune'
# req = requests.get(url)
# html = req.text

#token path
token_path = os.path.dirname(os.path.abspath(__file__)) + "/token.txt"
t = open(token_path,"r",encoding="utf-8")
token = t.read().split()[0]

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("심해"))

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("!링크"):
        await message.channel.send("hi")

"""
@bot.command()
async def 링크(ctx):
    await ctx.send(url)
"""

client.run(token)

#client.run('NzEzODI5ODk3NjAwMTA2NTc3.Xsl0DA.sLqw8o_855BJ5O2UGDFU8wvhOoI')
