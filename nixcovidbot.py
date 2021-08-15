import os
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType, component

bot = commands.Bot(command_prefix = "!")
Token = os.environ["Token"]
startup_extensions = ['cogs.Button_Covid']
os.chdir('/cogs')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{} : {}'.format(type(e).__name__, e)
            print('파일 로딩 실패 {}\n{}'.format(extension,exc))

@bot.event
async def on_ready():
    DiscordComponents(bot, change_discord_methods=True)
    print("Ready")

bot.run(Token)
