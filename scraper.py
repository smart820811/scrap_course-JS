from urllib import response
import requests
from bs4 import BeautifulSoup
# import json

response = requests.get('https://mis.taifex.com.tw/futures/RegularSession/EquityIndices/FuturesDomestic/')
print(response.text.find('臺指現貨'))
# print(response.json()['data'])