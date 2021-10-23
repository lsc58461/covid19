from bs4 import BeautifulSoup
import urllib.request

url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='

def datecr():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        datecr = soup.find('span', {'class': 't_date'}) #기준날짜
        print(f'기준일: {datecr.string}')

        return datecr
    except:
        return "Error"

def totalcovid():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        totalcovid = soup.select('dd.ca_value')[0].text #누적 확진자수
        print(f'누적 확진자: {totalcovid} 명')

        return totalcovid
    except:
        return "Error"

def todaytotalcovid():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        todaytotalcovid = soup.select('p.inner_value')[0].text #당일 확진자수 소계
        print(f'확진자 소계: {todaytotalcovid} 명')

        return todaytotalcovid
    except:
        return "Error"
        
def todaydomecovid():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        todaydomecovid = soup.select('p.inner_value')[1].text #당일 국내발생 확진자수
        print(f'국내발생: {todaydomecovid} 명')

        return todaydomecovid
    except:
        return "Error"
        
def todayforecovid():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        todayforecovid = soup.select('p.inner_value')[2].text #당일 해외유입 확진자수
        print(f'해외유입: {todayforecovid} 명')

        return todayforecovid
    except:
        return "Error"
        
def totalca():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        totalca = soup.select('dd.ca_value')[2].text #누적 격리해제
        print(f'누적 격리해제: {totalca} 명')

        return totalca
    except:
        return "Error"
        
def todayca():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        todayca = soup.select('span.txt_ntc')[0].text #당일 격리해제
        print(f'격리해제: {todayca} 명')

        return todayca
    except:
        return "Error"
        
def totalcaing():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        totalcaing = soup.select('dd.ca_value')[4].text #누적 격리중
        print(f'누적 격리중: {totalcaing}')

        return totalcaing
    except:
        return "Error"
        
def todaycaing():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        todaycaing = soup.select('span.txt_ntc')[1].text #당일 격리중
        print(f'격리중: {todaycaing} 명')

        return todaycaing
    except:
        return "Error"
        
def totaldead():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        totaldead = soup.select('dd.ca_value')[6].text #누적 사망자
        print(f'누적 사망자: {totaldead} 명')

        return totaldead
    except:
        return "Error"
        
def todaydead():
    try:
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        todaydead = soup.select('span.txt_ntc')[2].text #당일 사망자
        print(f'사망자: {todaydead} 명')

        return todaydead
    except:
        return "Error"
