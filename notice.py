import discord, asyncio, os, sys, setting, datetime

app = discord.Client()
Setting = setting.Settings()
afk = []

@app.event
async def on_ready():
    print("login" % ())
    
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
    
                id = message.author.id
    
                if message.author.id == Setting.bot_id:
                               return None
                
                if id in afk:
                    embed = discord.Embed(title="잠수 상태가 해제되었어요!", description=str(message.author.name) + "님께서 잠수 상태가 해제되셨습니다.", color=0x0000ff)
                    await app.send_message(message.channel, embed=embed)
                    afk.remove(id)
        
    
    
                if message.content.startswith('/게임'):
                    if message.author.server_permissions.administrator:
                        learn = message.content.replace('/게임', "")
                        await app.change_presence(game=discord.Game(name=learn))
                        await app.send_message(message.channel, "봇의 게임을 변경하였습니다.")

                if message.content.startswith("/온라인"):
                    embed=discord.Embed(title="Jenon BOT 온라인 상황", description=None, color=0x00ff00)
                    embed.add_field(name="I'm online!", value="이 메세지가 발신되지 않으면 Offline 입니다.")
                    embed.add_field(name="요청자", value="<@" + str(message.author.name) + ">")
                    await app.send_message(message.channel, embed=embed)  
                
                if message.content.startswith("/초대"):
                    await app.send_message(message.channel, str(message.author.name)+" 죄송합니다.이 봇은 본 서버 전용 봇으로 초대할 수 없습니다.")

                if message.content.startswith("/상태"):
                    if message.author.id == Setting.owner_id:
                        embed = discord.Embed(title="Jenon Bot 서버 상태", color=0x00ff00)
                        embed.add_field(name="Owner id", value=Setting.owner_id, inline=True)
                        embed.add_field(name="classic log channel id", value=Setting.err_loging_channel, inline=True)
                        embed.add_field(name="Bot Notice Channel", value=Setting.notice_channel, inline=True)
                        embed.add_field(name="Welcome Channel", value=Setting.welcome_channel, inline=True)
                        embed.add_field(name="Ban User id", value=Setting.ban_user_id, inline=True)
                        await app.send_message(message.channel, embed=embed)
               
                if message.content.startswith('/도움말'):
                    a = datetime.datetime.today().year
                    b = datetime.datetime.today().month
                    c = datetime.datetime.today().day
                    d = datetime.datetime.today().hour
                    e = datetime.datetime.today().minute
                    f = datetime.datetime.today().second
                    embed=discord.Embed(title='`Jenon Bot 도움말 목록`', description=None, color=0xb2ebf4)
                    embed.add_field(name='`/온라인`', value='봇이 온라인인지 확인할 수 있습니다.', inline=False)
                    embed.add_field(name='`/도움말`', value='Jenon Bot 도움말을 출력합니다.', inline=False)
                    embed.add_field(name='`/초대`', value='Jenon Bot 초대링크를 출력하나, 이 봇은 서버 전용 봇으로 쓸모없는 커맨드((퍽퍽', inline=False)
                    embed.add_field(name='`/패치노트`', value="봇의 최근 업데이트 내용을 출력합니다.", inline=False)
                    embed.add_field(name='`/서버정보`', value="서버 정보를 출력합니다.", inline=False)
                    embed.add_field(name='`/잠수 [사유]`', value="잠수 상태에 돌입합니다. 사유도 넣을 수 있습니다.", inline=False)
                    embed.add_field(name='`/관리자 소개`', value="OverWatch discord Server | 서버 관리자들을 소개합니다!!!")
                    embed.set_footer(text="관리자 명령어는 '/관리자 도움말' 입력! | " + str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초")
                    await app.send_message(message.channel, embed=embed)

                if message.content.startswith('/관리자 도움말'):
                    embed=discord.Embed(title='`Jenon Bot 관리자 도움말 목록`', color=0x00ff00)
                    embed.add_field(name='/공지 [내용]', value="공지 채널에 내용을 공지로 전송합니다.")
                    embed.add_field(name='/종료', value='봇을 종료합니다.')
                    embed.add_field(name='/게임 [게임내용]', value='플레이중 상태를 [게임내용]으로 변경합니다.')
                    embed.add_field(name='/상태', value='Setting.py 및 서버 상태를 알려줍니다.')
                    await app.send_message(message.channel, embed=embed)

                if message.content.startswith("/서버정보"):
                    embed = discord.Embed(title="\"%s\" 서버정보!" % (message.server.name), description=None, color=0X00ff00)
                    embed.add_field(name="서버 소유자", value="<@%s>" % message.server.owner.id, inline=False)
                    embed.add_field(name="서버 생성일", value="%s (UTC)" % (message.server.created_at), inline=False)
                    embed.add_field(name="서버 보안등급", value=message.server.verification_level, inline=False)
                    embed.add_field(name="서버 위치", value=message.server.region, inline=False)
                    embed.add_field(name="서버 잠수채널", value="%s (%s분 이상 잠수이면 이동됨)" % (message.server.afk_channel, message.server.afk_timeout/60), inline=False)
                    embed.set_thumbnail(url=message.server.icon_url)
                    await app.send_message(message.channel, embed=embed)

                if message.content.startswith('/종료'):
                    embed = discord.Embed(title="메인 모듈 종료", color=0xff0000)
                    embed.add_field(name="The main module is change to offline.", value="요청자 : " + str(message.author.name))
                    await app.send_message(app.get_channel(Setting.err_loging_channel), embed=embed)
                    quit()

                if message.content.startswith('/관리자 소개'):
                    embed = discord.Embed(title="OverWatch discord의 관리자들을 소개합니다!", color=0xff0000)
                    embed.add_field(name="아루의 즐거운게임 천국", value="서버 주인(Server Owner)")
                    embed.add_field(name="Jenon", value="서버 관리자/봇 관리자(Server Adminstor/Bot manager)")
                    embed.set_footer(text="Project Bot : Jenon Bot")
                    await app.send_message(message.channel, embed=embed)

    
                if message.content.startswith("/공지"):
                    learn = message.content.replace('/공지', "")
                    if message.author.server_permissions.administrator:
                        a = datetime.datetime.today().year
                        b = datetime.datetime.today().month
                        c = datetime.datetime.today().day
                        d = datetime.datetime.today().hour
                        e = datetime.datetime.today().minute
                        f = datetime.datetime.today().second
                        g = message.author.name
                        embed = discord.Embed(title=str(g) + "님의 공지", color=0x00ff00)
                        embed.add_field(name=learn, value="관리자 권한 : 인증✅")
                        embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 | 발신자 : " + str(message.author.name))
                        await app.send_message(app.get_channel(Setting.notice_channel), embed=embed)
                        await app.send_message(message.channel, "완료!")
  
                if message.content.startswith('/잠수'):
                    learn = message.content.replace('/잠수', "")
                    a = datetime.datetime.today().year
                    b = datetime.datetime.today().month
                    c = datetime.datetime.today().day
                    d = datetime.datetime.today().hour
                    e = datetime.datetime.today().minute
                    afk.append(id)
                    if learn == '':
                        embed = discord.Embed(title="잠수 시작!", color=0x00ff00)
                        embed.add_field(name=(message.author.name) + "님의 잠수 상태가 시작되었습니다!!!", value="잠수 시작 시간 : " + str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분")
                        await app.send_message(message.channel, embed=embed)
                    else:
                        embed = discord.Embed(title="잠수 시작!", color=0x00ff00)
                        embed.add_field(name=(message.author.name) + "님의 잠수 상태가 시작되었습니다!!!", value="잠수 시작 시간 : " + str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분")
                        embed.add_field(name="사유", value=learn)
                        await app.send_message(message.channel, embed=embed)
                if message.content.startswith('/패치노트'):
                    embed = discord.Embed(title="업데이트 내역", color=0x00ff00)
                    embed.add_field(name="●일부 번역 작업", value="일부 구간에서 한국어를 영어로 번역하였습니다.")
                    embed.add_field(nane="●긴급수정:서버 안정화 작업", value="20191113 Update")
                    await app.send_message(message.channel, embed=embed)

                if "/" in message.content:
                    a = datetime.datetime.today().year
                    b = datetime.datetime.today().month
                    c = datetime.datetime.today().day
                    d = datetime.datetime.today().hour
                    e = datetime.datetime.today().minute
                    f = datetime.datetime.today().second
                    embed=discord.Embed(title="Jenon Bot Command log", description=str(message.author.name), color=0x0000ff)
                    embed.add_field(name="메세지 내용", value=(message.content))
                    embed.add_field(name="메세지 채널", value="<#" + str(message.channel.id) + ">")
                    embed.set_footer(text=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초에 발신됨.")
                    await app.send_message(app.get_channel(Setting.err_loging_channel), embed=embed)
                    print("Jenon Bot Command Use Log\n발신자:" + str(message.author.name) + "\n발신 서버 : " + str(message.server.name) + "\n내용 : " + str(message.content) % ())

access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
