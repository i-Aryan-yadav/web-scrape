import requests
from bs4 import BeautifulSoup
import time
import csv
import send_mail
from datetime import date

url=["https://finance.yahoo.com/quote/BTC-INR?p=BTC-INR&.tsrc=fin-srch","https://finance.yahoo.com/quote/ETH-INR?p=ETH-INR&.tsrc=fin-srch","https://finance.yahoo.com/quote/LTC-INR?p=LTC-INR&.tsrc=fin-srch","https://finance.yahoo.com/quote/DOGE-INR?p=DOGE-INR&.tsrc=fin-srch"]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.48"}

today= str(date.today())+ ' report' + '.csv'
csv_file=open(today,"w")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["STOCK NAME","CURRENT PRICE","PREVIOUS CLOSE","OPEN","DAY RANGE","52 WEEK RANGE","START DATE","ALGORITHM"])

for c in range(0,len(url)):
    stock=[]
    html_page= requests.get(url[c],headers=headers)
    soup=BeautifulSoup(html_page.content,"lxml")

    header_info=soup.find_all("div", id="quote-header-info")[0]
    stock_title=header_info.find("h1").get_text()
    stock_info=header_info.find("span").get_text()

    price_info=soup.find_all("div", class_="D(ib) Mend(20px)")[0]
    stock_price=price_info.find("span").get_text()

    stock.append(stock_title)
    stock.append(stock_price)



    #print("COMPANY NAME  :   ",stock_title )
    #print("")
    #print("BY            :   ",stock_info)
    #print("")
    #print("PRICE IN USD  :   ",stock_price)
    #print("")
    #print("SUMMARY  :  ")
   # print("")


    table_info=soup.find_all("div", class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")
#print(table_info.get_text())

    for i in range(0,12,2):
        #table_content1=table_info[0].find_all("td")[i].get_text()
        table_content2=table_info[0].find_all("td")[i+1].get_text()
        #print("table_content1","   -  ",table_content2 )
        #print("")
        stock.append(table_content2)
    #print("")
    #print("")
    time.sleep(5)
    csv_writer.writerow(stock)
print("done")
csv_file.close()

send_mail.send(file_name=today)
print ("sent")


