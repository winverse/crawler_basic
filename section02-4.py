import requests
from lxml.html import fromstring, tostring

def main():
  session = requests.Session()
  
  response = session.get('http://www.naver.com/')
  
  urls = scrape_news_list_page(response)

def scrape_news_list_page(response):
  urls = {}
  root = fromstring(response.content)
  
  root.make_links_absolute(response.url)

  for index, dom in enumerate(root.xpath('//div[@class="thumb_area"]/*')):
    newsNameDom = dom.xpath('//img[@class="news_logo"]')[index];
    newslinkDom = dom.xpath('//div[@class="popup_wrap"]/a[@class="btn_popup"]')[index];
    
    name = extract_name(newsNameDom)
    link = extract_link(newslinkDom)
    
    urls[name] = link

  print(urls)
    
def extract_link(dom):
  link = dom.get('href')
  return link

def extract_name(dom):
  name = dom.get('alt')
  return name

if __name__ == '__main__':
  main()