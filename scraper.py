from urllib import response
import requests
from bs4 import BeautifulSoup
# import json

response = requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20220527&selectType=30&_=1653814046068')
# print(response.headers['Content-Type'])
print(response.json()['data'])