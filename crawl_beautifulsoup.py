from bs4 import BeautifulSoup


def search_something(text, tagname, *classname):
  print(f'search with bs4 : {classname}')
  soup = BeautifulSoup(text, 'html.parser')
  classname_str = '.'.join(classname)
  print(f'{tagname}.{classname_str}')
  #tag.get_text()로 사용할 수 있음
  #tag.get_text().replace('\n\n\n','\n')
  return [tag.text.replace('\n\n\n','\n') for tag in soup.select(f'{tagname}.{classname_str}')]
