import urllib.request
import urllib.parse
import ssl

context = ssl._create_unverified_context()

API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
# https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1014
params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

for c in params:
  param = urllib.parse.urlencode(c)
  url = API + "?" + param
  print("url =", url)
  
  res_data = urllib.request.urlopen(url, context=context).read()
  
  contents = res_data.decode("utf-8")
  
  print(contents)