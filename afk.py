import discord, asyncio, setting, datetime

client = discord.Client()
Setting = setting.Settings()
afk = []

@client.event
async def on_ready():
    print("완료" % ())
    
@client.event
async def on_message(message):
    id = message.author.id
    if message.author.id == Setting.bot_id:
        return None
    if message.author.id == Setting.ban_user_id:
        await client.send_message(message.channel, "당신은 봇관리자에 의해 차단된 유저입니다! \n 문의는 봇관리자 개인메세지로 주세요.\n Jenon{Xenon} 제논 [Melon™]")
        await client.send_message(client.get_channel(Setting.err_loging_channel), "차단된 유저가 명령어 사용을 시도하였습니다.\n유저 이름 : %d\n유저 아이디 : %d\n사용 서버 : %d\nCN Bot Logger")
    
    if id in afk:
        embed = discord.Embed(title="잠수 상태가 해제되었어요!", description=str(message.author.name) + "님께서 잠수 상태가 해제되셨습니다.", color=0x0000ff)
        await client.send_message(message.channel, embed=embed)
        afk.remove(id)

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
            embed.add_field(name=(message.author.name) + "님의 잠수 상태가 시작되었습니다!!!", value="잠수 시작 시간 : " + str(a) + "년" + str(b) + "월" + str(c) + "일" + str(d) + "시" + str(e) + "분")
            await client.send_message(message.channel, embed=embed)
        else:
            embed = discord.Embed(title="잠수 시작!", color=0x00ff00)
            embed.add_field(name=(message.author.name) + "님의 잠수 상태가 시작되었습니다!!!", value="잠수 시작 시간 : " + str(a) + "년" + str(b) + "월" + str(c) + "일" + str(d) + "시" + str(e) + "분")
            embed.add_field(name="사유", value=learn)
            await client.send_message(message.channel, embed=embed)

    if message.content.startswith('/기능 종료 잠수'):
        embed = discord.Embed(title="잠수 모듈 종료", color=0xff0000)
        embed.add_field(name="잠수 모듈 종료", value="요청자 : " + str(message.author.name))
        await client.send_message(client.get_channel(Setting.err_loging_channel), embed=embed)
        quit()

client.run("NTQ3NDEzOTcxMjAwOTAxMTIw.XOI5Wg.1pKHZRbctSJ8SRrpYCxwna5ASxA")
