from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_links(page_link):
    
  page = urlopen(page_link)
  soup = BeautifulSoup(page, 'html.parser')


  name_box = soup.find_all('div', attrs={'class': 'results-i'})

  data = []
  for i in name_box:
      if i.text.__contains__("PROQRAM"):
        link = i.find('a', attrs={'class': 'results-i-link'})
        data.append( 'https://boss.az' + link['href'])


  print(data)
quote_page = 'https://boss.az/vacancies?action=index&controller=vacancies&only_path=true&search%5Bcategory_id%5D=38&type=vacancies'

get_links(quote_page)