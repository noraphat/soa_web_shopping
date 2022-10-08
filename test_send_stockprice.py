from bs4 import BeautifulSoup
import requests
from songline import Sendline
token = 'ACRwZ6dSgOHePJlKl46D9hufiIdcoa9OXaYnxuS5dXS' 
messenger = Sendline(token)


def get_price_stock(company_name):
    url = f'https://www.finnomena.com/stock/{company_name}'
    res = requests.get(url)
    res.encoding = 'utf-8'
    price_stock_name = ""
    if res.status_code == 200:
        soup = BeautifulSoup(res.text,'html.parser')
        price_stock = soup.find_all('h2')
        price_stock_name = str(price_stock[0].string)
        #print(price_stock_name)
    else:
        print('Http response code is :' +str(res.status_code))
    return price_stock_name

stock_list = ['advanc','bbl','aot','bem']
for x in stock_list:
    stock_price = get_price_stock(x)
    str_line = 'ราคาหุ้นของบริษัท' +x+ 'คือ :' +stock_price
    print('ราคาหุ้นของบริษัท' +x+ 'คือ :' +stock_price)
    messenger.sendtext(str_line)