import discord
from discord.ext import commands, tasks
from pathlib import Path



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


global auth = 0
client = commands.Bot(command_prefix ='.')
status = ['jammin' , 'eating' , 'sleeping']
ID = ""
Pass = ""
#=======================================MUSIC SECTION==================================


#=======================================COMMAND AND EVENT=================================================

@tasks.loop(seconds = 20) #working
async def change_status():
    await client.change_presence(activity = discord.Game(choice(status)))

@client.event #not tested
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general": # We check to make sure we are sending the message in the general channel
            await channel.send_message(f"""Welcome to the server {member.mention}""")

@client.event #not tested
async def on_member_join(member):
    Role = discord.utilis.get(member.server.roles , name = 'FRIENDS')
    await client.add_roles(member,role)

@client.event #working
async def on_ready() :
    change_status.start()
    print("bot is online")
    print('logged in as')
    print(client.user.name)

@client.command(name = 'ping', help = 'this command return the latency') #working
async def ping (ctx) :
   await ctx.send(f'**Pong !** Latency: {round(client.latency * 10000)}ms')

@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
    await ctx.send(choice(responses))

@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
    await ctx.send(choice(responses))

#=================================================ILEARN SEC===========================================================================
@client.command(name = 'login name', help = 'to store oneID and Password if u are Richard, the creator') #working
@commands.has_role("Richard Wibowo")
async def login(ctx):
    global ID 
    ID = "46112820"
    global Pass 
    Pass = "Dkx3.wkDWe8pfK9"
    await ctx.send('hi, richard')
    print(ID) 
    print(Pass)

@client.command(name = 'check oneID', help = 'send oneID i inputed') #not working
async def check(ctx):
    await ctx.send(ID)
    print(Pass)
    await ctx.send("check terminal for pass <3 ")

@client.command(name = 'open ilearn' , help = 'to open ilearn fast') #working
async def open(ctx): 
     
     #open ilearn
    await ctx.send('Please study now')

    Webdriver = "D:\Key Log\Discord-bot\chromedriver.exe"
    driver = webdriver.Chrome(Webdriver)
    driver.get("https://ilearn.mq.edu.au/login/index.php")

        #pass login
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.clear
    password.clear
    username.send_keys(ID)
    password.send_keys(Pass)
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()




client.run('NzgwMzIxNzcyMDMzMTQ2ODgx.X7tZSA.3cbobs0zYrTiuK6n4aI9Ybc2HAg')

