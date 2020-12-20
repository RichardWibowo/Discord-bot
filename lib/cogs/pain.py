from discord.ext.commands import Cog
from discord.ext.commands import command
from random import choice
from discord.ext import tasks

class pain(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name = 'ping', help = 'this command return the latency')
    async def ping (ctx) :
        await ctx.send(f'**Pong !** Latency: {round(client.latency * 10000)}ms')

    @command(name='hello', help='This command returns a random welcome message')
    async def hello(ctx):
        responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
        await ctx.send(choice(responses))

    @command(name='die', help='This command returns a random last words')
    async def die(ctx):
        responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
        await ctx.send(choice(responses))

    @Cog.listener()
    async def on_ready(self):
	    if not self.bot.ready:
		    self.bot.cogs_ready.ready_up("Pain")



def setup(bot):
	bot.add_cog(pain(bot))


