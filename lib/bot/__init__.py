from asyncio import sleep
from datetime import datetime
from glob import glob

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord import Embed, File, DMChannel
from discord import Intents
from discord.errors import HTTPException, Forbidden
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument,
								  CommandOnCooldown)
from discord.ext.commands import when_mentioned_or, command, has_permissions

from ..db import db

PREFIX = "-"
OWNER_ID = [709231814748930099]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]
IGNORE_EXCEPTIONS = (CommandNotFound, BadArgument)

class Ready(object):
	def __init__(self):
		for cog in COGS:
			setattr(self, cog, False)

	def ready_up(self, cog):
		setattr(self, cog, True)
		print(f" {cog} cog ready")

	def all_ready(self):
		return all([getattr(self, cog) for cog in COGS])




class Bot(BotBase):
    def __init__(self): 
        self.PREFIX = PREFIX                     #adding prefix as an atribute
        self.ready = False  
        self.cogs_ready = Ready()                #check later if the bot is ready or not later
        self.guild = None                        #to define
        self.scheduler = AsyncIOScheduler()      #to schedule our bot
        
        db.autosave(self.scheduler)

        super().__init__(
            command_prefix = PREFIX,
            owner_id = OWNER_ID,
            intents = Intents.all(),
         ) #creating the bot
   
    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f" {cog} cog loaded")
        print("setup complete")

    def run(self,version):
            self.VERSION = version

            print("begin assembling remnants")
            self.setup()

            with open("./lib/bot/token.0" , "r", encoding="utf-8") as tf:
                self.TOKEN = tf.read()

            print("drawing the summoning circle...")
            super().run(self.TOKEN, reconnect = True)

    async def process_commands(self, message):
        ctx = await self.get_context(message, cls=Context)
        await self.invoke(ctx)

    async def on_connect(self):
        print("assembling physical body")

    async def on_disconnect(self):
        print("the hero has slain the bot")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong.")
        await self.stdout.send("An error occured.")
        # type: ignore
        raise 

    async def on_command_error(self, ctx, exc):  
        if any([isinstance(exc, error) for error in IGNORE_EXCEPTIONS]):
           pass

        elif isinstance(exc, MissingRequiredArgument):
           await ctx.send("One or more required arguments are missing.")

        elif hasattr(exc,"original") :
            if isinstance(exc.original, Forbidden):
                await ctx.send("I do not have permission to do that.")
            else:
                raise exc.original

        else :
            raise exc
    
    async def print_message(self):
            #await self.stdout.send("wake up rise and shine, its time to code again ")
            pass

    async def on_ready(self):
        if not self.ready :
            self.guild = self.get_guild(779601376773799977)
            self.stdout = channel= self.get_channel(789901396165918750)
            self.scheduler.add_job(self.print_message, CronTrigger(second=0))
            self.scheduler.start()
            embed = Embed(title="Now online!", description="bot is now online.",
					  colour=0xFF0000, timestamp=datetime.utcnow())
			# fields = [("Name", "Value", True),
			# 		  ("Another field", "This field is next to the other one.", True),
			# 		  ("A non-inline field", "This field will appear on it's own row.", False)]
			# for name, value, inline in fields:
			# 	embed.add_field(name=name, value=value, inline=inline)
			# embed.set_author(name="Carberra Tutorials", icon_url=self.guild.icon_url)
			# embed.set_footer(text="This is a footer!")
            await channel.send(embed = embed)

			# await channel.send(file=File("./data/images/profile.png"))
            
            await self.stdout.send("Now online!")
            self.ready = True
            print(" bot ready")
            
        else:
            print("your bot at your service")

    async def on_message(self,message):
        if not message.author.bot :
            await self.process_commands(message)

bot = Bot()

    

