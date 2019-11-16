import discord, sys, os, json, asyncio, datetime, logging, sqlite3
from datetime import datetime
from discord.ext import commands


logging.basicConfig(format="%(levelname)s -- %(name)s.%(funcName)s : %(message)s", level=logging.INFO)
print(os.getcwd())
try:
    with open("configuration.json", "r") as f:
        conf = json.load(f)
except IOError:
    print("Config???")
    sys.exit()
    
startup_ext = conf['cogs']
prefixes = ["x","X","..."]




#https://discordapp.com/channels/494095601403691009/494121829800214538/557633639928561714																					
NR = commands.AutoShardedBot(command_prefix ="X", shard_count=conf['shards'])

for extension in startup_ext:
    try:
        NR.load_extension(extension)
        print(extension)
    except Exception as e:
        print(e)
		
@NR.event						
async def on_ready():
    print('Logged in as:')
    print('{0.user}'.format(NR))

@NR.command()
async def echo(ctx, *, data):
    await ctx.send(data)

NR.run(conf['token_black'])