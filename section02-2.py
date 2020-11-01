import urllib.request as req
from urllib.error import URLError, HTTPError

path_list = ["/Users/openknowl_sanghyun/Desktop/test1.jpg", "/Users/openknowl_sanghyun/Desktop/index.html"]

# 다운로드 리소스 URL
target_url = ["http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg",
              "http://google.com"]

for i, url in enumerate(target_url):
  try:
    res = req.urlopen(url)
    contents = res.read()
    
    with open(path_list[i], 'wb') as c:
      c.write(contents)
  
  except HTTPError as e:
    print(e)
  except URLError as e:
    print(e)
  else:
    print('------------')
    print('success')