from random import choice, randint
from typing import Optional
from discord.ext import commands

import googletrans
from aiohttp import request
from discord import Member, Embed
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown
from googletrans.models import Translated

class SearchEngine(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name = "dictionary", aliases = ['dic'], help = "to search at miriam and wordnik dictionary ")
    async def dictionary(self, ctx, word):
        await ctx.send(f'Source1: https://www.merriam-webster.com/dictionary/{word}')
        await ctx.send(f'Source2: <https://www.wordnik.com/words/{word}>')
    
    @command(name = 'translate', alliases =['tr'], help = 'to translate using google translate')
    async def translate(self, ctx, lang_to, *args):
        lang_to = lang_to.lower()
        if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
            raise commands.BadArgument("Invalid language to translate text to")

        text = ' '.join(args)
        translator = googletrans.Translator()
        text_translated = translator.translate(text, dest=lang_to).text
        await ctx.send(text_translated)
    
    @Cog.listener()
    async def on_ready(self):
        print("SearcEngine == OK! ")
        if not self.bot.ready:
           self.bot.cogs_ready.ready_up("SearchEngine")

def setup(bot):
	bot.add_cog(SearchEngine(bot))


