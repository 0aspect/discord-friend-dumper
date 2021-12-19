import discord

token = "your token here"
bot = commands.Bot(self_bot=True)
    
@bot.event
async def on_ready():
    print('dumping friends')
    f = open('friends.txt', 'a', encoding="utf-8")
    for user in bot.user.friends:
        f.write(f"{user.name}#{user.discriminator} | {user.id}\n")

bot.run(token, bot=False)
