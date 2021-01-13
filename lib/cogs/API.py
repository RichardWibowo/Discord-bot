from random import choice, randint
from typing import Optional

from aiohttp import request
from discord import Member, Embed
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown

class API(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name = "facts")
    async def animal_fact_API(self,ctx, animal : str):
        if animal.lower() in ("dog","cat", "panda", "koala", "fox"):
            factURL = f"https://some-random-api.ml/facts/{animal}"
            imageURL = f"https://some-random-api.ml/img/{animal}"

            async with request("GET",imageURL,headers={}) as response :
                if response.status == 200 :
                    data = await response.json()
                    image_link = data["link"]
                else :
                    image_link = None

            async with request("GET", factURL, headers = {})as response :
                if response.status == 200 :
                    data = await response.json()
                    embed = Embed(title=f"{animal.title()} fact", 
                                  description=data["fact"],
                                  colour=ctx.author.colour)
                    if image_link is not None:
                        embed.set_image(url=image_link)
                    await ctx.send(embed = embed)
                else :
                    await ctx.send(f"API returned a {response.status} status.")
        else :
            await ctx.send("just make them extinct please.")

    @command(name = "To Binary",aliases = ['bin', '01'], help = "to change user txt to binary")
    async def encrypt_API(self,ctx,message):
        encryptURL = f"https://some-random-api.ml/binary?text={message}"
        async with request("GET", encryptURL, headers = {})as response :
            if response.status == 200:
                data = await response.json()
                await ctx.message.delete()
                await ctx.send (f"{data} ***encrypt with binary***")
            else :
                await ctx.send("error detected")

    @command(name = "to Text", aliases = ['text', 'txt'], help = "to change user txt to utc")
    async def dencrypt_API(self,ctx,message):
        dencryptURL = f"https://some-random-api.ml/binary?decode={message}"
        async with request("GET", dencryptURL, headers = {})as response :
            if response.status == 200:
                data = await response.json()
                await ctx.message.delete()
                await ctx.send (f"{data} ***dencrypt with binary***")
            else :
                await ctx.send("error detected")


    @Cog.listener()
    async def on_ready(self):
        print("API COG == OK! ")
        if not self.bot.ready:
           self.bot.cogs_ready.ready_up("API")


def setup(bot):
	bot.add_cog(API(bot))