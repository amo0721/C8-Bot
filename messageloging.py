import discord, asyncio, os, setting, datetime

app = discord.Client()
Setting = setting.Settings()

@app.event
async def on_ready():
    print("Messageloging 기능을 활성화합니다." % ())

@app.event
async def on_member_join(member):
    embed = discord.Embed(title="환영해요!", description = None, color=0x0000ff)
    embed.add_field(name="유저 닉네임 : " + (member.name), value="유저 아이디 : " + (member.id))
    await app.send_message(app.get_channel(Setting.welcome_channel), embed=embed)

@app.event
async def on_member_remove(member):
    embed = discord.Embed(title="잘가요...ㅜㅜ", color=0x00ff00)
    embed.add_field(name="유저 닉네임 : " + (member.name), value="유저 아이디 : " + (member.id))
    await app.send_message(app.get_channel(Setting.welcome_channel), embed=embed)

@app.event
async def on_message(message):
    if message.author.id == Setting.bot_id: 
                   return None
    
    if message.content.startswith("/기능 종료 로그"):
        if message.author.server_permissions.administrator:
            embed = discord.Embed(title = "로그 종료", description = "로그 기능이 종료되었습니다.", color = 0xff0000)
            embed.add_field(name="Messageloging.py is down.", value="Messageloging.py 가 종료되었습니다.")
            await app.send_message(app.get_channel(Setting.err_loging_channel), embed=embed)
            quit()

     
    if "/" in message.content:
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        embed=discord.Embed(title="CN Bot Command log", description=str(message.author.name), color=0x0000ff)
        embed.add_field(name="메세지 내용", value=(message.content))
        embed.add_field(name="메세지 채널", value="<#" + str(message.channel.id) + ">")
        embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초에 발신됨.")
        await app.send_message(app.get_channel(Setting.err_loging_channel), embed=embed)

app.run("NTQ3NDEzOTcxMjAwOTAxMTIw.XOI5Wg.1pKHZRbctSJ8SRrpYCxwna5ASxA")
