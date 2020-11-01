import json
import requests

s = requests.Session()

r = s.get('http://httpbin.org/stream/100', stream=True)

# 수신 확인
# print(r.text)

# Encoding 확인
# print('Encoding: {}'.format(r.encoding))


# if r.encoding is None:
#   r.encoding = 'UTF-8'
  
# for line in r.iter_lines(decode_unicode=True):
#   b = json.loads(line)
#   print(b)
#   # print(type(b))

#   for k, v in b.items():
#     print("key: {}, values: {}".format(k, v))
    
#   print()
#   print()
  
s.close()
  
r = s.get('https://jsonplaceholder.typicode.com/posts/1')

print(r.headers)
print(r.text)

#JSON 변환
print(r.json())

# key 변환
print(r.json().keys())

# value 변환

print(r.json().values())

print(r.encoding)

s.close()


