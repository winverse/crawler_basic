import requests

s = requests.Session()

r = s.get('https://naver.com')

# print('1,', r.text)

print('status code {}'.format(r.ok))

# 세션 비활성화
# s.close()

s = requests.Session()

# r = s.get('http://httpbin.org/cookies', cookies={'name': 'niceman'})
# print(r.text)

#User-agent
# url = 'http://httpbin.org/get'
# headers = { 'user-agent': 'niceman_app_v1.0.0'}

# r = s.get(url, headers=headers)
# print(r.text)

s.close()

with requests.Session() as s:
  pass
  r = s.get('http://www.naver.com')
  print(r.text)
