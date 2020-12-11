from bs4 import BeautifulSoup


def search_something(tagname, classname, text):
  print(f'search with bs4 : {classname}')
  soup = BeautifulSoup(text, 'html.parser')
  for tag in soup.select(f'{tagname}.{classname}'):
    print(tag.text)

