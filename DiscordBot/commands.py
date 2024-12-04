import discord
import globals
from discord.ext import commands

# Get server status
@globals.bot.command()
@commands.has_role("Developer")
async def status(ctx):
    flag = False
    async with ctx.channel.typing():
        for addr in globals.AddressList:
            if globals.is_ping_catched(addr) == False:
                await ctx.send("[-] {} is DEAD".format(addr))
                flag = True
    if flag is False:
        await ctx.send("[+] Passed")
        await globals.bot.change_presence(activity=discord.Game("サーバー正常 : {}".format(globals.get_current_time())), status=discord.Status.online)  # ステータスの更新
    else:
        await globals.bot.change_presence(activity=discord.Game("サーバー異常 : {}".format(globals.get_current_time())), status=discord.Status.idle)

# Get IP Address
@globals.bot.command()
@commands.has_role("Developer")
async def getip(ctx):
    await ctx.send(globals.get_global_ip())