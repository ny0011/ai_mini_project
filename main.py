from crawl_request import read_webpage, find_something
from crawl_beautifulsoup import search_something

html_text = read_webpage('https://www.daum.net/')
find_something('class="link_favorsch @', html_text)
search_something('a','link_favorsch', html_text)