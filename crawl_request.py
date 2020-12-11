import requests


def read_webpage(link):
    print('read webpage')
    r = requests.get(link)
    print(f'status code : {r.status_code}')
    if r.status_code == requests.codes.ok:
      return r.text
    else:
      r.raise_for_status()


def find_something(sth, text):
    print(f'find {sth}')
    start = 0
    while text.find(sth, start) != -1:
      index = text.find(sth, start)
      start = text.find(">", index)
      end = text.find('</a>', start)
      print(text[start+1:end])