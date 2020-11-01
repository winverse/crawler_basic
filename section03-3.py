import json
import urllib.request as req
from fake_useragent import UserAgent
import ssl

ua = UserAgent(verify_ssl=False)

context = ssl._create_unverified_context()

headers = {
  'User-Agent': ua.ie,
  'referer': 'https://finance.daum.net/'
}

url = "https://finance.daum.net/api/search/ranks?limit=10"

# print(req.Request('http://finance.daum.net/api/search/ranks?limit=10'))

res = req.urlopen(req.Request(url, headers=headers), context=context).read().decode('utf-8')

rank_json = json.loads(res)['data']

print(rank_json, '\n')

for elm in rank_json:
  print('순위: {}, 금액: {}, 회사명: {}'.format(elm['rank'], elm['tradePrice'], elm['name']))