import globals
import discord
import subprocess
from discord.ext import tasks
from cloudflare_ddns import CloudFlare

# 自機を除いた監視対象のIPアドレス
AddressList = [ "192.168.1.51", "192.168.1.52", "192.168.1.55" ]

# 指定されたアドレスにPingを飛ばす
def is_host_alive(HostList):
    try:
        for i in HostList:
            result = subprocess.run(["ping", i,"-c","3", "-W", "300"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            if result.returncode != 0:
                return False
            
        return True
    except Exception as e:
        return False

# 5分に1回実行する
@tasks.loop(minutes=5) 
async def BackgroundTasks():

    # 各所にpingを飛ばす
    if is_host_alive(AddressList):
        await globals.bot.change_presence(activity=discord.Game("サーバー正常 : {}".format(globals.getTime())), status=discord.Status.online)
    else:
        await globals.bot.change_presence(activity=discord.Game("サーバー異常 : {}".format(globals.getTime())), status=discord.Status.idle)

    # CloudFlare DDNS
    for domain in globals.DomainList:
        cf = CloudFlare(globals.EMAIL, globals.API_KEY, domain)
        cf_record = cf.get_record("A", domain)

        if globals.get_global_ip().strip() not in cf_record["content"]:
            cf.sync_dns_from_my_ip()
            await globals.bot.get_channel(globals.DEV_CHANNEL_ID).send("CloudFlare : Update IP")