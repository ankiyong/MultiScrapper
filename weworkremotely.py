import requests
from bs4 import BeautifulSoup

def get_wewo_soup(word):
  url = f'https://weworkremotely.com/remote-jobs/search?term={word}'
  res = requests.get(url)
  soup = BeautifulSoup(res.text,'html.parser')
  item_box = soup.find('div',{'id':'job_list'}).find_all('ul')
  return item_box

def extract_wewo_jobs(word):
  url = 'https://weworkremotely.com/'
  info_dict = []
  item_box = get_wewo_soup(word)
  for item in item_box:
    box = item.find_all('li')
    for list in box:
      try:
        title = list.find('span',{'class':'title'}).text
        company = list.find('span',{'class':'company'}).text
        location = list.find('span',{'class':'region company'}).text
        link = url+list.find('a')['href']
        dict = {'title':title,
            'company':company,
            'location':location,
            'link':link}
        info_dict.append(dict)
      except:
        pass

  return info_dict
    
