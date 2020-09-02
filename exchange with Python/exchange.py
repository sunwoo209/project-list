from bs4 import BeautifulSoup
import requests
import pandas
import math
#아톰 에디터에서 한국어
import sys
import io
from tkinter import *

import xml.etree.ElementTree as ET
from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

today = datetime.today().strftime("%Y%m%d")# YYYYmmdd 형태의 시간 출력
today1 = datetime.today().strftime("%Y-%m-%d")


#한국은행 api 받아오기
Service = "StatisticSearch"
key = "B1A9VHXK31S5JBEK3X2P"
lang = "xml"
start = "1"
last = "1000"
code = "036Y001" #당일 환율 정보 코드
firstday = today #YYYYmmdd 의 형태 숫자로 넣어도 가능
lastday = today  #오전 9시 40분에 그날의 환율정보 초장 갱신  마감장 16시 30분 // # today 변수는
url = "http://ecos.bok.or.kr/api/"+Service+"/"+key+"/"+lang+"/kr/"+start+"/"+last+"/"+code+"/DD/"+firstday+"/"+lastday+"/"


ret = requests.get(url)
soup = BeautifulSoup(ret.text,'xml') #XML 이안불러와질때 pip install
data = soup.find_all('row')

Exchange = {}


for row in data:
    nation = row.find("ITEM_NAME1")
    value = row.find("DATA_VALUE")
    nation1 = nation.get_text()
    value1 = value.get_text()
    Exchange[nation1] = value1

E_usa = float(Exchange.get('원/미국달러(매매기준율)'))
E_china = float(Exchange.get('원/위안(매매기준율)'))
E_jp = float(Exchange.get('원/일본엔(100엔)'))
E_eu = float(Exchange.get('원/유로'))
E_uk = float(Exchange.get('원/영국파운드'))
E_canada = float(Exchange.get('원/캐나다달러'))
E_france = float(Exchange.get('원/스위스프랑'))
E_australia = float(Exchange.get('원/호주달러'))
E_newzealand = float(Exchange.get('원/뉴질랜드달러'))
E_hongkong = float(Exchange.get('원/홍콩달러'))


def K_input():
    #미국
    korea=float(e3.get())
    result1=math.floor((korea/E_usa))
    e5.delete(0, END)
    e5.insert(0, result1)
    #중국
    korea=float(e3.get())
    result2=math.floor((korea/E_china))
    e6.delete(0, END)
    e6.insert(0, result2)
    #일본
    korea=float(e3.get())
    result3=math.floor((korea/E_jp)*100)
    e7.delete(0, END)
    e7.insert(0, result3)
    #유로
    korea=float(e3.get())
    result4=math.floor((korea/E_eu))
    e8.delete(0, END)
    e8.insert(0, result4)
    #영국
    korea=float(e3.get())
    result5=math.floor((korea/E_uk))
    e9.delete(0, END)
    e9.insert(0, result5)
    #캐나다
    korea=float(e3.get())
    result6=math.floor((korea/E_canada))
    e10.delete(0, END)
    e10.insert(0, result6)
    #스위스
    korea=float(e3.get())
    result7=math.floor((korea/E_france))
    e11.delete(0, END)
    e11.insert(0, result7)
    #호주
    korea=float(e3.get())
    result8=math.floor((korea/E_australia))
    e12.delete(0, END)
    e12.insert(0, result8)
    #뉴질랜드
    korea=float(e3.get())
    result9=math.floor((korea/E_newzealand))
    e13.delete(0, END)
    e13.insert(0, result9)
    #홍콩
    korea=float(e3.get())
    result10=math.floor((korea/E_hongkong))
    e14.delete(0, END)
    e14.insert(0, result10)

def Exb5():
    i5=float(e5.get())
    trans=math.floor((i5*E_usa))
    e3.delete(0, END)
    e3.insert(0, trans)

def Exb6():
    i6=float(e6.get())
    trans=math.floor((i6*E_china))
    e3.delete(0, END)
    e3.insert(0, trans)

def Exb7():
    i7=float(e7.get())
    trans=math.floor((i7*E_jp/100))
    e3.delete(0, END)
    e3.insert(0, trans)

def Exb8():
    i8=float(e8.get())
    trans=math.floor((i8*E_eu))
    e3.delete(0, END)
    e3.insert(0, trans)

def Exb9():
    i9=float(e9.get())
    trans=math.floor((i9*E_uk))
    e3.delete(0, END)
    e3.insert(0, trans)

def Exb10():
    i10=float(e10.get())
    trans=math.floor((i10*E_canada))
    e3.delete(0, END)
    e3.insert(0, trans)

def Exb11():
    i11=float(e11.get())
    trans=math.floor((i11*E_france))
    e3.delete(0, END)
    e3.insert(0, trans)

def Exb12():
    i12=float(e12.get())
    trans=math.floor((i12*E_australia))
    e3.delete(0, END)
    e3.insert(0, trans)

def Exb13():
    i13=float(e13.get())
    trans=math.floor((i13*E_newzealand))
    e3.delete(0, END)
    e3.insert(0, trans)

def Exb14():
    i14=float(e14.get())
    trans=math.floor((i14*E_hongkong))
    e3.delete(0, END)
    e3.insert(0, trans)

def reset():
    e3.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)

window = Tk()

l1 = Label(window, text=today1)
l1.grid(row = 0, column = 0)
l1 = Label(window, text='환율 계산 프로그램')
l1.grid(row = 0, column = 1)
b1= Button(window, text="초기화", command=reset)
b1.grid(row = 0, column = 2)


empty1=Label(window, text="")
empty1.grid(row = 1, column = 1)

l3 = Label(window, text='원화')
l3.grid(row = 3, column = 0)
e3 = Entry(window)
e3.grid(row = 3, column = 1)
b3= Button(window, text="원화 환전", command=K_input)
b3.grid(row = 3, column = 2)

empty4=Label(window, text="")
empty4.grid(row = 4, column = 1)

#미국
l5 = Label(window, text='미국 달러')
l5.grid(row = 5, column = 0)
e5 = Entry(window)
e5.grid(row = 5, column = 1)
b5= Button(window, text="  ->  원화", command=Exb5)
b5.grid(row = 5, column = 2)
#중국
l6 = Label(window, text='중국/위안')
l6.grid(row = 6, column = 0)
e6 = Entry(window)
e6.grid(row = 6, column = 1)
b6= Button(window, text="  ->  원화", command=Exb6)
b6.grid(row = 6, column = 2)
#일본
l7 = Label(window, text='일본/엔')
l7.grid(row = 7, column = 0)
e7 = Entry(window)
e7.grid(row = 7, column = 1)
b7= Button(window, text="  ->  원화", command=Exb7)
b7.grid(row = 7, column = 2)
#유로
l8 = Label(window, text='유로')
l8.grid(row = 8, column = 0)
e8 = Entry(window)
e8.grid(row = 8, column = 1)
b8= Button(window, text="  ->  원화", command=Exb8)
b8.grid(row = 8, column = 2)
#파운드
l9 = Label(window, text='영국/파운드')
l9.grid(row = 9, column = 0)
e9 = Entry(window)
e9.grid(row = 9, column = 1)
b9 = Button(window, text="  ->  원화", command=Exb9)
b9.grid(row = 9, column = 2)
#캐나다
l10 = Label(window, text='캐나다 달러')
l10.grid(row = 10, column = 0)
e10 = Entry(window)
e10.grid(row = 10, column = 1)
b10 = Button(window, text="  ->  원화", command=Exb10)
b10.grid(row = 10, column = 2)
#스위스프랑
l11 = Label(window, text='스위스 프랑')
l11.grid(row = 11, column = 0)
e11 = Entry(window)
e11.grid(row = 11, column = 1)
b11= Button(window, text="  ->  원화", command=Exb11)
b11.grid(row = 11, column = 2)
#호주
l12 = Label(window, text='호주 달러')
l12.grid(row = 12, column = 0)
e12 = Entry(window)
e12.grid(row = 12, column = 1)
b12= Button(window, text="  ->  원화", command=Exb12)
b12.grid(row = 12, column = 2)
#뉴질랜드
l13 = Label(window, text='뉴질랜드 달러')
l13.grid(row = 13, column = 0)
e13 = Entry(window)
e13.grid(row = 13, column = 1)
b13= Button(window, text="  ->  원화", command=Exb13)
b13.grid(row = 13, column = 2)
#홍콩
l14 = Label(window, text='홍콩 달러')
l14.grid(row = 14, column = 0)
e14 = Entry(window)
e14.grid(row = 14, column = 1)
b14= Button(window, text="  ->  원화", command=Exb14)
b14.grid(row = 14, column = 2)



window.mainloop()
