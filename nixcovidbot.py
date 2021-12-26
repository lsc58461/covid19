import os
import discord
from Crawling_Covid import time, datecr, Total_Infection, Today_Infection, Vaccination_Status, Total_Death, Today_Death
from discord_components import DiscordComponents, Button, ButtonStyle, Select, Interaction, SelectOption
from discord.embeds import Embed

client = discord.Client()
DiscordComponents(client)

Token = os.environ['Token']

@client.event
async def on_ready():
	global lines
	now = datetime.datetime.now()
	with open('fword_list.txt', encoding="utf-8-sig") as f:
		data=f.readlines()
	lines = [line.rstrip('\n') for line in data]
	print("ready")

@client.event
async def on_message(msg):
	if msg.content == "!버튼":
		'''
        try:
            await msg.delete()
        except:
            pass
		'''
		await msg.channel.send(embed=discord.Embed(color=0xFF0F13, title="Covid-19 국내 현황", description="밑에 버튼을 눌러 알아보세요!", url='http://ncov.mohw.go.kr/').set_footer(text="상호작용 실패 오류 발생 시 다시 시도 해주세요!"), components=[[Button(label="🦠 확진환자", id="Confirmed_case", style=ButtonStyle.blue), Button(label="🩸 사망자", id="Death", style=ButtonStyle.red), Button(label="💉 예방접종현황", id="Vaccination_Status", style=ButtonStyle.green, disabled=False)]])

@client.event
async def on_button_click(interaction: Interaction):
	try:
		if interaction.component.custom_id == "Confirmed_case":
			await interaction.respond(type=5)
			embed = discord.Embed(title='🦠 확진환자',description="",color=0x368AFF).add_field(name='누적 확진자',value=f'{Total_Infection()} 명',inline=False).add_field(name='당일 확진자',value=f'{Today_Infection()} 명',inline=False).set_footer(text=datecr())
			print(f'{time()})  요청자: {interaction.user.name}\n------------------------')
			await interaction.respond(embed=embed)
	except:
		embed = discord.Embed(title='BT_1 Error',description="잠시 후 다시 시도해주세요\n오류가 계속 될 시 문의 바랍니다.",color=0xFF0F13)
		await interaction.respond(embed=embed)
	try:
		if interaction.component.custom_id == "Death":
			await interaction.respond(type=5)
			embed = discord.Embed(title='🩸 사망자',description="",color=0xFF0F13).add_field(name='누적 사망자',value=f'{Total_Death()} 명',inline=False).add_field(name='당일 사망자',value=f'{Today_Death()} 명',inline=False).set_footer(text=datecr())
			print(f'{time()})  요청자: {interaction.user.name}\n------------------------')
			await interaction.respond(embed=embed)
	except:
		embed = discord.Embed(title='BT_2 Error',description="잠시 후 다시 시도해주세요\n오류가 계속 될 시 문의 바랍니다.",color=0xFF0F13)
		await interaction.respond(embed=embed)
	try:
		if interaction.component.custom_id == "Vaccination_Status":
			await interaction.respond(type=5)
			_Vaccination_Status = Vaccination_Status()
			embed = discord.Embed(title='💉 예방접종현황',description="",color=0x1DDB16,).add_field(name='1차 접종',value=f'{_Vaccination_Status[0]}',inline=True).add_field(name='누적 1차 접종',value=f'{_Vaccination_Status[2]} 명',inline=True).add_field(name='신규 1차 접종',value=f'{_Vaccination_Status[3]} 명',inline=True).add_field(name='접종 완료',value=f'{_Vaccination_Status[1]} 명',inline=True).add_field(name='누적 접종 완료',value=f'{_Vaccination_Status[4]} 명',inline=True).add_field(name='신규 접종 완료',value=f'{_Vaccination_Status[5]} 명',inline=True).set_footer(text=datecr())
			print(f'{time()})  요청자: {interaction.user.name}\n------------------------')
			await interaction.respond(embed=embed)
	except:
		embed = discord.Embed(title='BT_3 Error',description="잠시 후 다시 시도해주세요\n오류가 계속 될 시 문의 바랍니다.",color=0xFF0F13)
		await interaction.respond(embed=embed)

@client.event
async def on_message(message): ##### remove bad words
	try:
		if message.author == client.user:
			return
		else:
			message_contant = message.content
			for i in lines:
				if i in message_contant:
					MyEmbed = Embed(
						title = "비속어 감지",
						color = 0xFF4848
					)MyEmbed.add_field(
						name = "────────────────────────",
						value = f"{message.author.mention}님이 비속어 [{i}]을(를) 사용하셨습니다.\n────────────────────────",
						inline = True
					)
					if i == "":
						return
					else:
						await message.channel.send('어머')
						await message.channel.send(embed=MyEmbed)
						await message.delete()
	except:
		print("비속어 에러")
		return
	
client.run(Token)
