import globals
import subprocess
from discord.ext import commands

AllAddressList = [ "192.168.1.51", "192.168.1.52", "192.168.1.55" ]

# Get server status
@globals.bot.command()
async def status(ctx):
    status_code = 0
    try:
        for addr in AllAddressList:
            result = subprocess.run(["ping", addr,"-c","3", "-W", "300"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode != 0:
                status_code = 1
                await ctx.send("[-] {} is DEAD".format(addr))
    except Exception as e:
        status_code = 1
        await ctx.send("[-] {} is DEAD".format(addr))

    if status_code == 0:
        await ctx.send("[+] Passed")

# Get IP Address
@globals.bot.command()
async def getip(ctx):
    await ctx.send(globals.get_global_ip())