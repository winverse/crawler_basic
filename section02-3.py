import requests
import lxml.html

def main():
    response = requests.get('https://www.naver.com/')
    urls = scrape_news_list_page(response)
    for a in urls:
      print(a)
        
  
def scrape_news_list_page(res):
  urls = [];
  root = lxml.html.fromstring(res.content)
  
  for a in root.cssselect('.popup_wrap a.btn_popup'):
    url = a.get('href')
    if url != '#':
      urls.append(url)
  return urls


if __name__ == '__main__':
  main()