import requests


def read_webpage(link):
    print('read webpage')
    r = requests.get(link)
    print(f'status code : {r.status_code}')
    if r.status_code == requests.codes.ok:
      #r.content로 사용할 수 있음
      return r.text
    else:
      r.raise_for_status()


