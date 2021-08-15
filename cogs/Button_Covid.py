import discord
import urllib.request
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType, component
from bs4 import BeautifulSoup

class Button_Covid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="!Covid_버튼생성")
    async def Covid(self, ctx):
        url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        datecr = soup.find('span', {'class': 't_date'}) #기준날짜
        print(f'기준일: {datecr.string}')

        totalcovid = soup.select('dd.ca_value')[0].text #누적 확진자수
        print(f'누적 확진자: {totalcovid} 명')

        todaytotalcovid = soup.select('p.inner_value')[0].text #당일 확진자수 소계
        print(f'확진자 소계: {todaytotalcovid} 명')

        todaydomecovid = soup.select('p.inner_value')[1].text #당일 국내발생 확진자수
        print(f'국내발생: {todaydomecovid} 명')

        todayforecovid = soup.select('p.inner_value')[2].text #당일 해외유입 확진자수
        print(f'해외유입: {todayforecovid} 명')

        totalca = soup.select('dd.ca_value')[2].text #누적 격리해제
        print(f'누적 격리해제: {totalca} 명')

        todayca = soup.select('span.txt_ntc')[0].text #당일 격리해제
        print(f'격리해제: {todayca} 명')

        totalcaing = soup.select('dd.ca_value')[4].text #누적 격리중
        print(f'누적 격리중: {totalcaing}')

        todaycaing = soup.select('span.txt_ntc')[1].text #당일 격리중
        print(f'격리중: {todaycaing} 명')

        totaldead = soup.select('dd.ca_value')[6].text #누적 사망자
        print(f'누적 사망자: {totaldead} 명')

        todaydead = soup.select('span.txt_ntc')[2].text #당일 사망자
        print(f'사망자: {todaydead} 명')   
        one = Button(label="🦠 확진환자", style=ButtonStyle.blue, id="Embed1")
        two = Button(label="😷 격리중", style=ButtonStyle.blue, id="Embed2")
        three = Button(label="😂 격리해제", style=ButtonStyle.blue, id="Embed3")
        four = Button(label="🩸 사망자", style=ButtonStyle.red, id="Embed4")

        Embed1 = discord.Embed(title='코로나19 국내 발생현황',description="",color=0xFF0F13).add_field(name='🦠 확진환자',value=f'{totalcovid}({todaytotalcovid}) 명'f'\n\n국내발생: {todaydomecovid} 명'f'\n해외유입: {todayforecovid} 명',inline=False).set_footer(text=datecr.string)

        Embed2 = discord.Embed(title='코로나19 국내 발생현황',description="",color=0xFF0F13,).add_field(name='😷 격리중',value=f'{totalcaing}({todaycaing}) 명',inline=False).set_footer(text=datecr.string)

        Embed3 = discord.Embed(title='코로나19 국내 발생현황',description="",color=0xFF0F13).add_field(name='😂 격리해제',value=f'{totalca}({todayca}) 명',inline=False).set_footer(text=datecr.string)
    
        Embed4 = discord.Embed(title='코로나19 국내 발생현황',description="",color=0xFF0F13).add_field(name='🩸 사망자',value=f'{totaldead}({todaydead}) 명',inline=False).set_footer(text=datecr.string)

        await ctx.send(
            embed = discord.Embed(title='코로나19 국내 발생현황',description="",color=0xFF0F13,url='http://ncov.mohw.go.kr/').set_footer(text="밑에 버튼을 눌러 알아보세요!"),
            components=[
                [one],
                [two],
                [three],
                [four]
            ]
        )

        buttons = {
            "Embed1": Embed1,
            "Embed2": Embed2,
            "Embed3": Embed3,
            "Embed4": Embed4
        }

        while True:
            event = await self.bot.wait_for("button_click")
            url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, "html.parser")

            datecr = soup.find('span', {'class': 't_date'}) #기준날짜
            print(f'기준일: {datecr.string}')

            totalcovid = soup.select('dd.ca_value')[0].text #누적 확진자수
            print(f'누적 확진자: {totalcovid} 명')

            todaytotalcovid = soup.select('p.inner_value')[0].text #당일 확진자수 소계
            print(f'확진자 소계: {todaytotalcovid} 명')

            todaydomecovid = soup.select('p.inner_value')[1].text #당일 국내발생 확진자수
            print(f'국내발생: {todaydomecovid} 명')

            todayforecovid = soup.select('p.inner_value')[2].text #당일 해외유입 확진자수
            print(f'해외유입: {todayforecovid} 명')

            totalca = soup.select('dd.ca_value')[2].text #누적 격리해제
            print(f'누적 격리해제: {totalca} 명')

            todayca = soup.select('span.txt_ntc')[0].text #당일 격리해제
            print(f'격리해제: {todayca} 명')

            totalcaing = soup.select('dd.ca_value')[4].text #누적 격리중
            print(f'누적 격리중: {totalcaing}')

            todaycaing = soup.select('span.txt_ntc')[1].text #당일 격리중
            print(f'격리중: {todaycaing} 명')

            totaldead = soup.select('dd.ca_value')[6].text #누적 사망자
            print(f'누적 사망자: {totaldead} 명')

            todaydead = soup.select('span.txt_ntc')[2].text #당일 사망자
            print(f'사망자: {todaydead} 명')      
            if event.channel is not ctx.channel:                # wait for the button click, get the button id
                return
            if event.channel == ctx.channel:
                response = buttons.get(event.component.id)     
                if response is None:
                    await event.channel.send(
                        "Something went wrong. Please try it again."            # error
                    )
                if event.channel == ctx.channel:
                    await event.respond(    
                        type=InteractionType.ChannelMessageWithSource,      # send the message
                        embed=response
                    )

def setup(bot):
    bot.add_cog(Button_Covid(bot))
