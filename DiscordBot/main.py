import discord
import globals
import tasks
import commands # 必要

# ログイン時のアクション
@globals.bot.event
async def on_ready():
    await globals.bot.change_presence(activity=discord.Game("起動 : " + globals.getTime())) # ??? をプレイ中
    print("[{}] Login success!".format(globals.getTime()))
    tasks.BackgroundTasks.start()

# メッセージ受信時
@globals.bot.event
async def on_message(message):
    # 他のBotからのメッセージはスルー
    if message.author.bot:
        return

    # これがないと ! 系のコマンドが動作しない
    await globals.bot.process_commands(message)

# メイン
if __name__ == "__main__":
    globals.bot.run(globals.TOKEN)