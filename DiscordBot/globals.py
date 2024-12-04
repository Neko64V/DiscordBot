import os
import pytz
import discord
import requests
import datetime
import subprocess
from ping3 import ping
from discord.ext import commands

# Bot TOKEN
TOKEN = 'DISCORD BOT TOKEN'

# Bot Setting
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True)
bot.remove_command("help")

# Chennnel
DEV_CHANNEL_ID = 000000000000000

# 自機を除いた監視対象のIPアドレス
AddressList = [ "192.168.1.51", "192.168.1.52", "192.168.1.55" ]

# WakeOnLAN MacAddress
WOL_MAC_ADDR = 'MAC ADDRESS' # 00:00:00:***

# 各種関数
def get_current_time():
    return datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y/%m/%d %H:%M:%S")
    
def get_global_ip():
    return requests.get('https://ifconfig.me').text

def is_windows():
    return os.name == "nt"

def is_ping_catched(address):
    try:
        if is_windows():
            if ping(address, timeout=1, unit='ms') is None:
                return False
        else:
            result = subprocess.run(["ping", address,"-c","1", "-W", "300"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode != 0:
                return False
        return True
    except Exception as e:
        return False