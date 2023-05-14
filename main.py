import discord
import random
from discord import *

# dont know what the fuck the intents part does but it works
bot = discord.Bot(intents=discord.Intents.all())

# STUFF

# does the activity. took me way too fucking long to figure this out with pycord
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="#HelloBoys", url="https://ligmaspoons.tk"))

# LISTS

# --- reply lists ---

# for the /randomquote command. i ran out of fucking ideas
quotes = ("'**the fuck are deez bitches doin' here?**' - *JTR 2023*", "'**guys, guys, let's do bidding...**' - *JTR 2023*", "'**wassup danger-**' - *JTR 2023*", "'**he just gives off dorky vibes**' - *JTR 2023*", "'**was he a creepy pervert in y5?**' - *JTR 2023*")

# jerome says when he agrees:
agree = ("exactly!!", "i would definitely agree", "that is certainly correct", "i have never heard something more true in my entire life - and im not alive", "jerome would like this opinion", "heck yeah, you're right", "for once, you're right in saying that", "that is the coldest take ever, it's obviously true!", "obviously!!", "harbin is certainly whatever you just said", "what do i say again? oh yeah, whatever you said is 100% true.")

# jerome says when he disagrees
disagree = ("no way!!!", "not in a million years", "im gonna have to call you in for that one", "we all know that i would never agree with this")

# when jerome's name is mentioned (very fucking annoying feature btw)
saymyname = ("""Jerome Bot, Jerome Bot,
Does whatever a JTR can
Shits out text, any length,
Replies whenever you don't want
Look Out!
Here comes Jerome Bot.

Is he smart?
Listen bud,
He's got spaghetti code DNA.
Can he sing, a balkan song?
Just type /balkan in the box
Hey, there
There goes Jerome Bot.
""")

# --- trigger lists ---

# dont ask
nwords = ("nig", "trigger", "ninja", "knicker", "vicar", "slipper", "slicker", "critter", "snigger", "neg", "nag", "superior", "suprem", "white")

# every word trigger. is it inefficient as shit? yes. so why are you keeping it? yes.
triggers = ("nig", "trigger", "ninja", "knicker", "vicar", "slipper", "slicker", "critter", "snigger", "neg", "nag", "skill issue", "ratio", "simmer", "L", "trash", "bad", "goofy", "brokie", "broke", "french", "fr", " ik", "zip", "average", "jerome", "fuck", "mom", "harbin", "clone", "superior", "suprem", "white")

# MESSAGE EVENTS

# behold, the world's shittiest code. does it work? just about.
@bot.event
async def on_message(message):
  if not message.author.bot:
    if not str(message.author.id) == "what the fuck i forgot to write something here. whatever i guess":
        if "skill issue" in message.content.lower() or "ratio" in message.content.lower() or "L " in message.content.lower() or "simmer" in message.content.lower() or "L" in message.content or "trash" in message.content.lower() or "bad" in message.content.lower() or "goofy" in message.content.lower():
            await message.channel.send(":laughing: says :index_pointing_at_the_viewer: you, <@" + str(message.author.id) + ">")
        elif "brokie" in message.content.lower() or "broke" in message.content.lower():
            await message.channel.send("haha! brokey :nerd:")
        elif "french" in message.content.lower():
            await message.channel.send("french??? :flag_fr:")
        elif "fr" in message.content.lower():
            await message.channel.send("wait, for real? :scream:")
        elif "ik" in message.content.lower():
            await message.channel.send("but do you, :nerd:")
        elif "zip" in message.content.lower():
            await message.channel.send(":zipper_mouth:")
        elif "average" in message.content.lower():
            await message.channel.send("average goofy ahh :duck: rambunxious :tada: individual :man_facepalming: (GARI) :nerd:")
        elif "jerome" in message.content.lower():
            await message.channel.send("""Jerome Bot, Jerome Bot,
Does whatever a JTR can
Shits out text, any length,
Replies whenever you don't want
Look Out!
Here comes Jerome Bot.

Is he smart?
Listen bud,
He's got spaghetti code DNA.
Can he sing, a balkan song?
Just type /balkan in the box
Hey, there
There goes Jerome Bot.
""")
        for nword in nwords:
            if nword in message.content.lower():
                await message.channel.send("<@" + str(message.author.id) + """>
    https://cdn.discordapp.com/attachments/1046385651924353036/1107358076849373184/rapidsave.com_in_a_parallel_universe-rxrfdfqq2qya1.mov""")
        if "fuck" in message.content.lower():
            await message.channel.send("fuck me? nahh :flag_fr:")
        elif "mom" in message.content.lower():
            await message.channel.send("who's mom? :girl:")
        elif "harbin" in message.content.lower() or "crazy" in message.content.lower():
            if "sexy" in message.content.lower() or "handsome" in message.content.lower() or "nice" in message.content.lower() or "epic" in message.content.lower() or "clever" in message.content.lower() or "smart" in message.content.lower() or "intelligent" in message.content.lower() or "shrexy" in message.content.lower() or "booty" in message.content.lower() or "breedable" in message.content.lower():
                await message.channel.send(random.choice(disagree) + " <@" + str(message.author.id) + ">")
            else:
                await message.channel.send(random.choice(agree) + " <@" + str(message.author.id) + ">")
        elif "clone" in message.content.lower():
            await message.channel.send("yeah, I'm actually jerome's clone, <@" + str(message.author.id) + ">")
    elif str(message.author.id) == "720203963806253136":
        for trigger in triggers:
            if trigger in message.content.lower():
                await message.channel.send("""shut up <@890982522538835978>
        don't talk to the robot version of yourself
        fucking narcissist.
        amirite, <@758408107369168946>?""")
                break # break out the loop otherwise itll be insulting jerome for every fucking trigger it meets - we only want it once
    else:
        await message.channel.send("your user id is fucked up... I don't wanna talk to you.") # this condition should never be met lol

# COMMANDS

# send the bot's latency'
@bot.command(description="sends me latency")
async def ping(ctx):
    if not ctx.user.id == "720203963806253136":
        await ctx.respond(f"my latency is {bot.latency * 1000} :skull:, like, bruh...")
    else:
        await ctx.respond("""shut up <@890982522538835978>
don't talk to the robot version of yourself
fucking narcissist.
amirite, <@758408107369168946>?""")

# gives a random greeting to the user. ran out of fucking ideas here as well.
@bot.command(description="gives you a greeting")
async def greet(ctx):
    greetings = ("hello there", "oh hey, we were just talking about you")
    await ctx.respond(random.choice(greetings))

# gives you a 'says you' message with emojis
@bot.command(description="self explanatory")
async def saysyou(ctx):
    await ctx.respond(":laughing: says :index_pointing_at_the_viewer: you")

# gives you 'a likely story' with emojis
@bot.command(description="for when someone is being a bit rambunxious")
async def likelystory(ctx):
    await ctx.respond("a likely :nerd: story :muscle: ")

# posts the original jerome picture as a file (uploads it to discord)
@bot.command(description="post original jerome pic")
async def jerome(ctx):
    await ctx.respond(file=discord.File('jerome.jpg'))

# gives you a random jerome quote. he's said a lot of stupid shit
@bot.command(description="post a random jerome quote")
async def randomquote(ctx):
    await ctx.respond(random.choice(quotes))

# BUTTONS

# dont know how the fuck this works but it does and im too scared to nerf it
class MyView(discord.ui.View):
    @discord.ui.button(label="ALBANIA", style=discord.ButtonStyle.primary, emoji="🇦🇱")
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("""RED AND BLACK I DRESS
WITH AN EAGLE ON MY CHEST
ALBANIA!
ALBANIA!""")

# prints lyrics for goofy ahh balkan songs
@bot.slash_command(description="print lyrics for famous balkan music")
async def balkans(ctx):
    await ctx.respond("CHOOSE:", view=MyView())

bot.run("MTA5Nzk2MTg5MjE0OTk4NTQxMA.GFVfgu.Gsz5f1L5VcVGqbQXYjcAcV2fMgxlUzbTrdw6kE")
