
import discord, random, json,requests,asyncio
from discord.ext import commands

     # create bot instance
bot = commands.Bot(command_prefix='!', description='jeth discord Bot By Juji')
     # load file into json and data define
o = json.load(open('jess.json','r',encoding='utf-8-sig'))
data = [(m['datestamp'],m['content']) for m in o]
	 # load commands txt 

     # login
@bot.event
async def on_ready():
    channel = discord.Object(id='channel ID Goes Here')
    print("Logged in as:  name={}, id={}".format( bot.user.name, bot.user.id ))


@bot.command(pass_context=True)
async def jeth(ctx):
    # Chooses a random quote
    content = random.choice(data)
    msg = "{}".format(content)
    await bot.say(msg)

async def my_background_task():
    await bot.wait_until_ready()
    channel = discord.Object(id='channel ID Goes Here)
    while not bot.is_closed:
        content = random.choice(data)
        msg = "Here is a thing I sayed before: {}".format(content)
        await bot.send_message(channel, msg)
        await asyncio.sleep(600) # task runs every 600 seconds

@bot.command(pass_context=True)
async def jethx(ctx, n: int = 1):
    """Chooses a random quote."""
    msg = ["{}".format(content) for content in [random.choice(data) for _ in range(0,n)]]
    await bot.say('\n'.join(msg))

@bot.command(pass_context=True)
async def search(ctx, phrase : str):
    # Match data with a search-phrase
    results = []
    for datestamp, content in data:
        if phrase in content: results.append( "{} \n{}\n".format(datestamp, content))
        if len(results) > 8: break

    if len(results) > 0:
        msg = "\n\n {}".format( "\n".join(results) )
    else:
        msg = "`  {} jeth Never Said That Before I Gayce`".format(phrase)
    await bot.say(msg)

bot.loop.create_task(my_background_task())

if __name__ == "__main__":
    try:
        bot.run('Bot Token Goes Here')
    except:
        pass
