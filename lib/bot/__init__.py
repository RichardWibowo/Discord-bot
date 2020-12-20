from asyncio import sleep
from datetime import datetime


from discord.ext.commands import Bot as BotBase

from discord.ext.commands import when_mentioned_or, command, has_permissions

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from glob import glob

from ..db import db

PREFIX = "."
OWNER_ID = [709231814748930099]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def wake_up(self,cog):
        setattr(self, cog, True)
        print(f"{cog} Cog ready")

    def complete_ring(self):
        return all([getattr(self, cog)]for cog in COGS)


class Bot(BotBase):
    def __init__(self): 
        self.PREFIX = PREFIX                     #adding prefix as an atribute
        self.ready = False  
        self.cogs_ready = Ready()                     #check later if the bot is ready or not later
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

    async def on_connect(self):
        print("assembling physical body")

    async def on_disconnect(self):
        print("the hero has slain the bot")

    async def on_error (self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("welp, ur on ur own buddy")
        raise 

    async def on_Command_error (self, err, exc):
        if isinstance(exc , CommandNotFound):
           await ctx.send("error 404 = command not found") 
           await self.stdout.send("error nanoraa") 
           pass

        elif hasattr(exc,"original") :
            raise exc.original

        else :
            raise exc
    
    async def print_message(self):
            await self.stdout.send("wake up rise and shine, its time to code again ")

    async def on_ready(self):
        if not self.ready :
            
            self.guild = self.get_guild(779601376773799977)
            self.stdout = channel= self.get_channel(783532237526138920)
            self.scheduler.add_job(self.print_message, CronTrigger(hour = 7, minute= 0, second = 0))
            self.scheduler.start()
            
            while not self.cogs_ready.complete_ring():
                await sleep(0.5)
                
            self.ready = True
            print("your bot has been summoned")
            await self.stdout.send("hi master")

            #embed = Embed(title = "now online", 
            #              description = "use me to learn ", 
            #              colour = 0xFF0000,
            #              timestamp = datetime.utcnow()
            #)
            #fields = [("name ", "Value", False),
            #          ("another","new", True),
            #          ("another","new", True)]

            #for name, value, inline in fields:
            #    embed.add_field(name = name, 
            #                    value = value, 
            #                    inline = inline)
            #    embed.set_author(name = "NIGHTMARENIGHTMARE", icon_url = self.guild.icon_url)
            #    embed.set_footer(text = "pay your tribute to RichardM#5268")
            #    embed.set_thumbnail(url = self.guild.icon_url)

            
            #await channel.send(embed = embed)
            

        else:
            print("your bot at your service")

    async def on_message(self,message):

        if not message.author.bot:
          await self.process_commands(message)

bot = Bot()

    

