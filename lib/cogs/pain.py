from random import choice, randint
from typing import Optional

from aiohttp import request
from discord import Member, Embed
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown

class pain(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def text_to_bits(self, text, encoding='ISO-8859-1', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

    async def text_from_bits(self, bits, encoding='ISO-8859-1', errors='surrogatepass'):
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

    @command(name='hello', help='This command returns a random welcome message')
    async def hello(self, ctx):
        responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
        await ctx.send(f"{choice(responses)}{ctx.author.mention}!")

    @command(name='die', help='This command returns a random last words')
    async def die(self, ctx) : 
        responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
        await ctx.send(f"{choice(responses)}{ctx.author.mention}!")
    
    @command(name = "punch" ,alliases = ["slap"])
    async def punch(self, ctx, member : Member, *, reasons : Optional[str] = "idk honestly"):
        await ctx.send(f"{ctx.author.display_name} slapped {member.mention} {reasons}!")

    @command(name = "lock", alliases =["lock", "enc"], help = "to lock with magic and sorcery")
    async def encrypt(self, ctx, *, text):
        x = await self.text_to_bits(text)
        lx = len(x)

        y = int(x,2) << 1
        y = bin(y)
        ly = len(y)

        diff = "".join("0" for x in range(lx - ly))
        y = diff+y

        d = await self.text_from_bits(y)
        _hex = hex(int.from_bytes(d.encode('ISO-8859-1', 'surrogatepass'), 'big'))
        _dec = int(_hex, 16)
        _bin = bin(int.from_bytes(d.encode('ISO-8859-1', 'surrogatepass'), 'big'))

        await ctx.send(f"```Hex Base16 : {_hex}\nDec Base10 : {_dec}\nBin Base2 : {_bin}```")

    @command(name = "unlock", alliases =["unlock", "denc"], help = "to unlock with magic and sorcery")
    async def decrypt(self, ctx, raw, base:int=0):
        if base == 0:
            if raw.startswith('0x'):
                value = 16
            elif raw.startswith('0b'):
                value = 2
            else:
                value = 10
        else: value = base

        y = int(raw,value) >> 1
        y = bin(y)

        await ctx.send(await self.text_from_bits(y))



    @Cog.listener()
    async def on_ready(self):
        print("pain cog == OK! ")
        if not self.bot.ready:
           self.bot.cogs_ready.ready_up("pain")



def setup(bot):
	bot.add_cog(pain(bot))


