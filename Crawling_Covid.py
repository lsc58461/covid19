import datetime
import urllib.request
from bs4 import BeautifulSoup

url = 'http://ncov.mohw.go.kr/'
url2 = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
def time():
    try:
        now = datetime.datetime.now()
        return now
    except:
        print('Time: Error')
        return 'Time Error'

def datecr():
    try:
        html = urllib.request.urlopen(url2)
        soup = BeautifulSoup(html, "html.parser")

        datecr = soup.find('span', {'class': 't_date'}) #기준날짜
        print(f'{time()})  기준일: {datecr.string}')

        return datecr.string
    except:
        print(f'{time()})  기준일: Error')
        return "Datecr Error"

def Total_Infection():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        Total_Infection = soup.select('div.box')[3].text #누적 확진자 수
        Total_Infection = Total_Infection.replace('\n', '')
        Total_Infection = Total_Infection.replace(' ', '')
        Total_Infection = Total_Infection.replace('(누적)확진', '')
        Total_Infection = Total_Infection.replace('다운로드', '')
        print(f'{time()})  누적 확진자: {Total_Infection} 명')

        return Total_Infection
    except:
        print(f'{time()})  누적 확진자: Error')
        return "Error"
    
def Today_Infection():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        Today_Infection = soup.select('td')[3].text #당일 확진자수 소계
        print(f'{time()})  당일 확진자: {Today_Infection} 명')

        return Today_Infection
    except:
        print(f'{time()})  당일 확진자: Error')
        return "Error"
        
def Vaccination_Status():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        First_Vaccination_Percent = soup.select('li.percent')[0].text #1차 접종 퍼센트
        
        Vaccination_Complete_Percent = soup.select('li.percent')[1].text #접종 완료 퍼센트
        
        Total_First_Vaccination_Complete = soup.select('li.person')[0].text #누적 1차 접종 수
        Total_First_Vaccination_Complete = Total_First_Vaccination_Complete.replace('누적', '')
        
        Today_First_Vaccination_Complete = soup.select('li.person')[1].text #신규 1차 접종 수
        Today_First_Vaccination_Complete = Today_First_Vaccination_Complete.replace(' ', '')
        Today_First_Vaccination_Complete = Today_First_Vaccination_Complete.replace('신규', '')
        
        Total_Vaccination_Complete = soup.select('li.person')[2].text #누적 접종 완료 수
        Total_Vaccination_Complete = Total_Vaccination_Complete.replace('누적', '')
        
        Today_Vaccination_Complete = soup.select('li.person')[3].text #신규 접종 완료 수
        Today_Vaccination_Complete = Today_Vaccination_Complete.replace(' ', '')
        Today_Vaccination_Complete = Today_Vaccination_Complete.replace('신규', '')
        
        print(f'{time()})  1차 접종 퍼센트: {First_Vaccination_Percent}')
        print(f'{time()})  접종 완료 퍼센트: {Vaccination_Complete_Percent}')
        print(f'{time()})  누적 1차 접종 수: {Total_First_Vaccination_Complete} 명')
        print(f'{time()})  신규 1차 접종 수: {Today_First_Vaccination_Complete} 명')
        print(f'{time()})  누적 접종 완료 수: {Total_Vaccination_Complete} 명')
        print(f'{time()})  신규 접종 완료 수: {Today_Vaccination_Complete} 명')

        return First_Vaccination_Percent, Vaccination_Complete_Percent, Total_First_Vaccination_Complete, Today_First_Vaccination_Complete, Total_Vaccination_Complete, Today_Vaccination_Complete
    except:
        print(f'{time()})  Vaccination_Status: Error')
        return "Error"
    
def Total_Death():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        Total_Death = soup.select('div.box')[2].text #누적 사망자
        Total_Death = Total_Death.replace('\n', '')
        Total_Death = Total_Death.replace(' ', '')
        Total_Death = Total_Death.replace('(누적)사망', '')
        print(f'{time()})  누적 사망자: {Total_Death} 명')

        return Total_Death
    except:
        print(f'{time()})  누적 사망자: Error')
        return "Error"
        
def Today_Death():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        Today_Death = soup.select('td')[0].text #당일 사망자
        print(f'{time()})  당일 사망자: {Today_Death} 명')

        return Today_Death
    except:
        print(f'{time()})  당일 사망자: Error')
        return "Error"
