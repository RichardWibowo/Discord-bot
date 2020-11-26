import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

auth = 0
client = commands.Bot(command_prefix ='.')

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general": # We check to make sure we are sending the message in the general channel
            await channel.send_message(f"""Welcome to the server {member.mention}""")

@client.event 
async def on_ready() :
    print ("bot is online")
    
@client.command
async def register(ctx) :
    await ctx.send('Please identify yourself')
    auth = input
    if(auth == 1) :
        username = 46112820
        password = "Dkx3.wkDWe8pfK9"
        print("hi, richard")

@client.command 
async def check(ctx) :
    print(username)
    print(password)


@client.command() 
async def open(ctx) : 
     
     #open ilearn
    await ctx.send('Please study now')
    PATH = "D:\Key Log\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://ilearn.mq.edu.au/login/index.php")

            #pass login
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.clear
    password.clear
    x = username 
    y = password
    username.send_keys(x)
    password.send_keys(y)
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

@client.command
async def ping (ctx) :
    await ctx.send('round(client.latency * 1000)ms')


client.run("NzgwMzIxNzcyMDMzMTQ2ODgx.X7tZSA.oJY8xYPH6mNheCpAXawfL3PuDlU")

