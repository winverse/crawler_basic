import urllib.request
from urllib.parse import urlparse
from urllib.error import URLError, HTTPError

url = 'http://www.encar.com'

mem = urllib.request.urlopen(url)

# print('type : {}'.format(type(mem)))
# print("geturl : {}".format(mem.geturl()))
# print("status : {}".format(mem.status))
# print("headers : {}".format(mem.getheaders()))
# print("getcode : {}".format(mem.getcode()))
# print("read : {}".format(mem.read(1).decode('utf-8'))) # 바이트 수
# print('parse : {}'.format(urlparse('http://www.encar.co.kr?test=test').query))

API = "http://api.ipify.org"

values = {
  'format': 'json'
}

print('before param : {}'.format(values))
params = urllib.parse.urlencode(values)
print('after param : {}'.format(params))

url = API + "?" + params
print("요청 url= {}".format(url))

# 수신 데이터 읽기
try: 
  data = urllib.request.urlopen(url).read()
  text = data.decode("utf-8")
  print('response : {}'.format(text))
except HTTPError as e:
  print('HTTPError', e)
except URLError as e:
  print('URLError', e)

# 수신 데이터 디코딩
