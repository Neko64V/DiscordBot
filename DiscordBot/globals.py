import pytz
import datetime
import requests
import discord
from discord.ext import commands

# Bot TOKEN
TOKEN = 'Your bot token'

# Bot Setting
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True)
bot.remove_command("help")

# CloudFlare
EMAIL = 'Email Addr'
API_KEY = 'CloudFlare - GLOBAL API KEY'
DomainList = [ "example.com", "example.com" ]

# Chennnel
DEV_CHANNEL_ID = 0000 # Rai's server. "開発者用"

# 各種関数
def getTime():
    return datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y/%m/%d %H:%M:%S")
    
def get_global_ip():
    return requests.get('https://ifconfig.me').text