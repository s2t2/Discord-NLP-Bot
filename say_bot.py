from nlp_lib import sentiment_score
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='/')
bot.description = "NLP Bot"


@bot.event
async def on_ready():
    print(f'[•] Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game('NLP'))
    print(f'[•] Playing NLP')


@bot.command()
async def sentiment(ctx, *, paragraph):
    """ Sentiment analysis based on arbitrary input.
    Output Range:
    • Very Positive
    • Positive
    • Sorta Positive
    • Neutral
    • Sorta Negative
    • Negative
    • Very Negative
    """
    await ctx.send(sentiment_score(paragraph))


def get_token():
    try:
        with open('./private-token.txt') as file:
            return file.readline()
    except FileNotFoundError:
        return input('Enter account token: ')


if __name__ == '__main__':
    bot.run(get_token())
