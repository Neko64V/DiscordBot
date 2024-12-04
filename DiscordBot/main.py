import discord
import globals
import tasks
import commands # 必要

# ログイン時のアクション
@globals.bot.event
async def on_ready():
    await globals.bot.change_presence(activity=discord.Game("起動 : " + globals.get_current_time())) # ??? をプレイ中
    tasks.BackgroundTasks.start()
    print("[{}] Login success!".format(globals.get_current_time()))
   
# メッセージ受信時
@globals.bot.event
async def on_message(message):
    # 他のBotからのメッセージはスルー
    if message.author.bot:
        return

    # ここで特定のワードが入っていた場合メッセージの削除等、言論統制が可能

    # これがないと各種コマンドが動作しない
    await globals.bot.process_commands(message)

# メイン
if __name__ == "__main__":
    globals.bot.run(globals.TOKEN)