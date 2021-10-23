import os
import discord
from Crawling_Covid import datecr, totalcovid, todaytotalcovid, todaydomecovid, todayforecovid, totalca, todayca, totalcaing, todaycaing, totaldead, todaydead
from discord_components import DiscordComponents, Button, ButtonStyle, Select, Interaction, SelectOption

client = discord.Client()
DiscordComponents(client)

Token = os.environ['Token']

@client.event
async def on_message(msg):
	if msg.content == "!버튼":
            try:
                await msg.delete()
            except:
                pass
            await msg.channel.send(embed=discord.Embed(color=0xFF0F13, title="코로나19 국내 발생현황", description="", url='http://ncov.mohw.go.kr/').set_footer(text="밑에 버튼을 눌러 알아보세요!"), components=[[Button(label="🦠 확진환자", id="Confirmed_case", style=ButtonStyle.blue), Button(label="😷 격리중", id="Quarantine", style=ButtonStyle.blue), Button(label="😂 격리해제", id="Quarantine_release", style=ButtonStyle.blue), Button(label="🩸 사망자", id="Death", style=ButtonStyle.red)]])

@client.event
async def on_button_click(interaction: Interaction):
	try:
		if interaction.component.custom_id == "Confirmed_case":
			_datecr = datecr()
			_datecr = _datecr.string
			_totalcovid = totalcovid()
			_todaytotalcovid = todaytotalcovid()
			_todaydomecovid = todaydomecovid()
			_todayforecovid = todayforecovid()
			embed = discord.Embed(title='코로나19 국내 발생현황',description="",color=0xFF0F13).add_field(name='🦠 확진환자',value=f'{_totalcovid}({_todaytotalcovid}) 명'f'\n\n국내발생: {_todaydomecovid} 명'f'\n해외유입: {_todayforecovid} 명',inline=False).set_footer(text=_datecr)
			await interaction.respond(embed=embed)
	except:
		await interaction.respond("BT_1 Error : 오류가 계속 될 시 문의 바랍니다.")
	try:
		if interaction.component.custom_id == "Quarantine":
			_datecr = datecr()
			_datecr = _datecr.string
			_totalcaing = totalcaing()
			_todaycaing = todaycaing()
			embed = discord.Embed(title='코로나19 국내 발생현황',description="",color=0xFF0F13,).add_field(name='😷 격리중',value=f'{_totalcaing}({_todaycaing}) 명',inline=False).set_footer(text=_datecr)
			await interaction.respond(embed=embed)
	except:
		await interaction.respond("BT_2 Error : 오류가 계속 될 시 문의 바랍니다.")
	try:
		if interaction.component.custom_id == "Quarantine_release":
			_datecr = datecr()
			_datecr = _datecr.string
			_totalca = totalca()
			_todayca = todayca()
			embed = discord.Embed(title='코로나19 국내 발생현황',description="",color=0xFF0F13).add_field(name='😂 격리해제',value=f'{_totalca}({_todayca}) 명',inline=False).set_footer(text=_datecr)
			await interaction.respond(embed=embed)
	except:
		await interaction.respond("BT_3 Error : 오류가 계속 될 시 문의 바랍니다.")
	try:
		if interaction.component.custom_id == "Death":
			_datecr = datecr()
			_datecr = _datecr.string
			_totaldead = totaldead()
			_todaydead = todaydead()
			embed = discord.Embed(title='코로나19 국내 발생현황',description="",color=0xFF0F13).add_field(name='🩸 사망자',value=f'{_totaldead}({_todaydead}) 명',inline=False).set_footer(text=_datecr)
			await interaction.respond(embed=embed)
	except:
		await interaction.respond("BT_4 Error : 오류가 계속 될 시 문의 바랍니다.")
    		
@client.event
async def on_ready():
	print("ready")

client.run(Token)
