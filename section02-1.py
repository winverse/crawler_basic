# Section02-1
# 파이썬 크롤링
# urllib 사용법 및 기본 스크래핑

import urllib.request as req

img_url = 'http://postfiles.pstatic.net/20120504_153/ilovepha_1336106563736SdC2T_JPEG/79225766.jpg?type=w3'
html_utl = 'http://google.com'

save_path1 = '/Users/openknowl_sanghyun/Desktop/hello.jpg'
save_path2 = '/Users/openknowl_sanghyun/Desktop/hello.html'

try:
  file1, header1 = req.urlretrieve(img_url, save_path1)
  file2, header2 = req.urlretrieve(html_utl, save_path2)
except Exception as e:
  print(e)
else:
  print(header1)
  print(header2)
  
  print('filename1 {}'.format(file1))
  print('filename2 {}'.format(file2))