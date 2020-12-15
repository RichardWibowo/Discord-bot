from datetime import datetime
from discord import Intents,Embed

from discord.ext.commands import Bot as Bot_basic
from discord.ext.commands import CommandNotFound
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from ..db import db

PREFIX = "."
OWNER_ID = [709231814748930099]

class Bot(Bot_basic):
    def __init__(self): 
        self.PREFIX = PREFIX                     #adding prefix as an atribute
        self.ready = False                       #check later if the bot is ready or not later
        self.guild = None                        #to define
        self.scheduler = AsyncIOScheduler()      #to schedule our bot
        
        db.autosave(self.scheduler)

        super().__init__(
            command_prefix = PREFIX,
            owner_id = OWNER_ID,
            intents = Intents.all(),
         ) #creating the bot

    def run(self,version):
        self.VERSION = version
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
           pass

        elif hasattr(exc,"original") :
            raise exc.original

        else :
            raise exc

    async def on_ready(self):
        if not self.ready :
            self.ready = True
            self.guild = self.get_guild(779601376773799977)
            self.scheduler.start()
            print("your bot has been summoned")

            channel = self.get_channel(783532237526138920)
            await channel.send("hello master")

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
        pass

bot = Bot()

    

