import requests

s = requests.Session()

r = s.get('http://api.github.com/events')

# 수신 상태 체크
r.raise_for_status()

# print(r.text)

# 쿠키 설정
jar = requests.cookies.RequestsCookieJar()

jar.set('name', 'niceman', domain='httpbin.org', path='/cookies')

# 요청2
r = s.get('http://httpbin.org/cookies', cookies=jar)

# 요청3

r = s.get('https://github.com', timeout=5)

# print(r.text)

# 헤더 정보
# print(r.headers)

# 예제5
payload1 = {'name': 'kim', 'pay': 'true'}
payload2 = (('name', 'park'), ('pay', 'false'))


r = s.post('http://httpbin.org/post', data=payload2)

# print(r.text)

r = s.put('http://httpbin.org/put', data={'data': '{"name": "Kim", "grade": "A"}'})

# print(r.text)

r = s.delete('http://httpbin.org/delete')

print(r.text)

s.close()