from crawl_request import read_webpage
from crawl_beautifulsoup import search_something

def find_something(text, sth):
  print(f'find {sth}')
  start = 0
  # 정규식 re 모듈로 '@\d+\">(.+)<' 이렇게 찾을 수 있음
  while text.find(sth, start) != -1:
    index = text.find(sth, start)
    start = text.find(">", index)
    end = text.find('</a>', start)
    print(text[start+1:end])

html_text = read_webpage('https://www.daum.net/')
find_something(html_text, 'class="link_favorsch @')

list_favorsch = search_something(html_text, 'ul','list_favorsch')
list_favorsch_hide = search_something(html_text, 'ul','list_favorsch', 'hide')
top5 = list(set(list_favorsch) - set(list_favorsch_hide))
print(''.join(top5))