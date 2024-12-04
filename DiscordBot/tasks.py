import globals
import discord
from discord.ext import tasks
from cloudflare_ddns import CloudFlare

# CloudFlare
EMAIL = '****@gmail.com'
API_KEY = 'CF - API KEY'
DomainList = [ "example.com", "example.net" ]

def is_allserver_alive(HostList):
    for address in HostList:
        if globals.is_ping_catched(address) == False:
            return False
    return True

# 5分に1回実行する
@tasks.loop(minutes=5)
async def BackgroundTasks():

    # サーバーのステータス更新
    if is_allserver_alive(globals.AddressList):
        await globals.bot.change_presence(activity=discord.Game("サーバー正常 : {}".format(globals.get_current_time())), status=discord.Status.online)  # 緑 (オンライン)
    else:
        await globals.bot.change_presence(activity=discord.Game("サーバー異常 : {}".format(globals.get_current_time())), status=discord.Status.idle)    # オレンジ (退席中)

    # CloudFlare DDNS
    for domain in DomainList:
        cf = CloudFlare(EMAIL, API_KEY, domain)
        record = cf.get_record("A", domain)

        # レコードと現在のIPアドレスが異なったら
        if globals.get_global_ip().strip() not in record["content"]:
            cf.sync_dns_from_my_ip()
            await globals.bot.get_channel(globals.DEV_CHANNEL_ID).send("CloudFlare : {} Updated IP".format(domain))