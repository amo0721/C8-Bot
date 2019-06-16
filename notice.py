import discord, asyncio, os, sys, setting, datetime

app = discord.Client()
Setting = setting.Settings()

@app.event
async def on_ready():
    print("공지 기능 활성화." % ())

@app.event
async def on_message(message):
    if message.author.id == Setting.bot_id:
                   return None
    if message.content.startswith("/공지 긴급패치"):
        learn = message.content.replace('/공지 긴급패치', "")
        if message.author.server_permissions.administrator:
            a = datetime.datetime.today().year
            b = datetime.datetime.today().month
            c = datetime.datetime.today().day
            d = datetime.datetime.today().hour
            e = datetime.datetime.today().minute
            f = datetime.datetime.today().second
            g = message.author.name
            embed = discord.Embed(title=str(g) + "님의 긴급패치 공지", color=0x00ff00)
            embed.add_field(name=learn, value="Module by Mary")
            embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 | 발신자 : " + str(message.author.name))
            await app.send_message(app.get_channel(Setting.notice_channel), embed=embed)
            await app.send_message(message.channel, "완료!")
    
    if message.content.startswith("/공지 업데이트"):
        learn = message.content.replace('/공지 업데이트', "")
        if message.author.server_permissions.administrator:
            a = datetime.datetime.today().year
            b = datetime.datetime.today().month
            c = datetime.datetime.today().day
            d = datetime.datetime.today().hour
            e = datetime.datetime.today().minute
            f = datetime.datetime.today().second
            g = message.author.name
            embed = discord.Embed(title=str(g) + "님의 봇 업데이트 공지", color=0x00ff00)
            embed.add_field(name=learn, value="Module by Mary")
            embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 | 발신자 : " + str(message.author.name))
            await app.send_message(app.get_channel(Setting.notice_channel), embed=embed)
            await app.send_message(message.channel, "완료!")

    if message.content.startswith("/공지 일반"):
        learn = message.content.replace('/공지 일반', "")
        if message.author.server_permissions.administrator:
            a = datetime.datetime.today().year
            b = datetime.datetime.today().month
            c = datetime.datetime.today().day
            d = datetime.datetime.today().hour
            e = datetime.datetime.today().minute
            f = datetime.datetime.today().second
            g = message.author.name
            embed = discord.Embed(title=str(g) + "님의 공지", color=0x00ff00)
            embed.add_field(name=learn, value="Module by Mary")
            embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 | 발신자 : " + str(message.author.name))
            await app.send_message(app.get_channel(Setting.notice_channel), embed=embed)
            await app.send_message(message.channel, "완료!")



    if message.content.startswith('/기능 종료 공지'):
        embed = discord.Embed(title="공지 모듈 종료", color=0xff0000)
        embed.add_field(name="공지 모듈 종료", value="요청자 : " + str(message.author.name))
        await app.send_message(app.get_channel(Setting.err_loging_channel), embed=embed)
        quit()

                        


app.run("NTQ3NDEzOTcxMjAwOTAxMTIw.XOI5Wg.1pKHZRbctSJ8SRrpYCxwna5ASxA")
