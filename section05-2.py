import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
import ssl

from bs4 import BeautifulSoup

context = ssl._create_unverified_context()

ssl._create_default_https_context = ssl._create_unverified_context

# Header 정보 초기화
opener = req.build_opener()

# User-Agent 정보
opener.add_handler = [('User-agent', UserAgent(verify_ssl=False).chrome)]

req.install_opener(opener)

# # 네이버 이미지 기본 URL(크롬 개발자 도구)

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="

quote = rep.quote_plus('지수')

# # URL 완성
url = base + quote

print('Request URL: {}'.format(url))

res = req.urlopen(url, context=context)

savePath = '~/Desktop/download/'

try:
  if not (os.path.isdir(savePath)):
    os.makedirs(os.path.join(savePath))
except OSError as e:
  # 에러 내용
  print("folder creation failed!")
  print("folder name : {}".format(e.filename))
  
  # 런타임 에러 raise
  raise RuntimeError('System Exit!')
else:
  print('folder created!')
  
soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("div.img_area > a.thumb._thumb > img")


for i, img_list in enumerate(img_list, 1):
  fullFileName = os.path.join('/Users/openknowl_sanghyun/Desktop/download', str(i) + '.png')
  # 파일명 출력 
  print('full name : {}'.format(fullFileName))
  
  # 다운로드 요청(URL, 저장경로)
  req.urlretrieve(img_list['data-source'], fullFileName)
  
# 다운로드 완료 시 출력
print("download succeeded!")
