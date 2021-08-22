import requests
from bs4 import BeautifulSoup

def get_remo_soup():
  URL = "https://remoteok.io/remote-python-jobs"
  headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
  res = requests.get(URL,headers=headers)
  soup = BeautifulSoup(res.text,'html.parser')
  item_box = soup.find('table',{'id':'jobsboard'})
  box = item_box.find_all('td',{'class':'company position company_and_position'})
  return box
def extract_remo_job(box):
  url = 'https://remoteok.io/remote-jobs/'
  job = []
  for info in box:
    try:
      company = info.find('h3',{'itemprop':'name'}).text
      title = info.find('h2',{'itemprop':'title'}).text
      location = info.find('div',{'class':'location tooltip'}).text
      link = url+info.find('a',{'itemprop':'url'})['href']
      
      dict = {'title':title,
            'company':company,
            'location':location,
            'link':link}
      job.append(dict)
    except:
      pass
  return job

# soup = get_soup()
# print(extract_job(soup))


