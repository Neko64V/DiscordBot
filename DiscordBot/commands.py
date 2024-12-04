import os
import discord
import globals
import subprocess
from yt_dlp import YoutubeDL
from discord.ext import commands

# CommandList
@globals.bot.command()
async def cmd(ctx):
    await ctx.send("""```
# everyone
・ytdl [タイトル] [YouTubeのリンク]

# developer
・GetIP
・Status              
・WakeOnLAN
```""")

# YouTubeの動画を .mp3にして送信
@globals.bot.command()
@commands.has_role("Developer")
async def ytdl(ctx, title, url):

    # URLが無効
    if 'https://' not in url:
        await ctx.send("URLが無効です。")
        return

    options = {
        'format': 'bestaudio/audio',
        'outtmpl': title,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'}]}

    # 時間かかる…
    async with ctx.channel.typing():
        with YoutubeDL(options) as ydl:
            try:
                ydl.download([url])
            except:
                await ctx.send("音声のダウンロードに失敗しました…")
                return
        await ctx.channel.send("{} の準備ができました！{}".format(title, ctx.author.mention), file=discord.File(title + '.mp3'))

    # Clean up
    await ctx.message.delete()
    os.remove(title + '.mp3')

# VCで流したい場合：
# チェック
#if ctx.voice_client is None:
#    VC = await ctx.author.voice.channel.connect()
#    if not VC:
#        return

# 再生
#AudioSource = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(title + ".mp3"), volume=0.5)
#ctx.voice_client.play(AudioSource)

# Get IP Address
@globals.bot.command()
@commands.has_role("Developer")
async def getip(ctx):
    await ctx.send(globals.get_global_ip())

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

# WakeOnLAN
@globals.bot.command()
@commands.has_role("Developer")
async def wakeonlan(ctx):
    args = [ 'wakeonlan', globals.WOL_MAC_ADDR]
    try:
        subprocess.check_call(args)
    except:
        await ctx.send("コマンドの送信に失敗")
    await ctx.send("PCを起動します")