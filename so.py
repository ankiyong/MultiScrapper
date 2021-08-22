import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
def last_so_page(url):
  result = requests.get(url,headers = headers)
  soup = BeautifulSoup(result.text,'html.parser')
  pages = soup.find('div',{'class':'s-pagination'}).find_all('a',{'class':'s-pagination--item'})
  max_page = pages[-2].get_text(strip=True)
  return max_page

def get_so_job(soup):
  info_dict = []
  item_box = soup.find('div', {'class': 'listResults'}).find_all('div', {'class': 'd-flex'})
  for item in item_box:
    url = "https://stackoverflow.com/jobs/"
    dict = {}
    title = item.find('a',{'s-link stretched-link'})
    name = item.find('h3', {'class': 'fc-black-700 fs-body1 mb4'})
    links = item.find('div')
    try:
      titles = title.text
      link = url + links['data-jobid']
      companies, location = name.find_all('span', recursive=True)
      company_name = companies.get_text(strip=True)
      location_name = location.get_text(strip=True)
      dict = {'title':titles,
              'comapny':company_name,
              'location':location_name,
              'link':link}
      info_dict.append(dict)
    except:
      pass
  return info_dict


def extract_so_jobs(last,url):
  jobs = []
  for i in range(1,int(last)+1):
    result = requests.get(f"{url}&pg={i+1}",headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    jobs_info = get_so_job(soup)
    for job in jobs_info:
      jobs.append(job)
  return jobs

def get_so_jobs(word):
  url = f"https://stackoverflow.com/jobs?r=true&q={word}"
  last_page = last_so_page(url)
  jobs = extract_so_jobs(last_page,url)
  return jobs