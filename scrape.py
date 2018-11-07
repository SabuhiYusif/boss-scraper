# import libraries
from urllib.request import urlopen
# from urllib.error import urlopen
from bs4 import BeautifulSoup

quote_page = 'https://boss.az/vacancies?action=index&controller=vacancies&only_path=true&search%5Bcategory_id%5D=38&type=vacancies'

page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')


name_box = soup.find_all('div', attrs={'class': 'results-i'})

# print(name_box.find('h3', attrs = {'class': 'results-i-title'}))
# links =
data = []
for i in name_box:
    if i.text.__contains__("PROQRAM"):
      link = i.find('a', attrs={'class': 'results-i-link'})
      data.append( 'https://boss.az' + link['href'])


print(data)
# print(name_box)
# name = name_box.text.strip()  # strip() is used to remove starting and trailing

# print(name)
# print(name_box.__contains__("PROQRAMÇI"))
# name = name_box.text.strip()  # strip() is used to remove starting and trailing
# print(name)

# quote_page = [
#     'https://boss.az/vacancies?action=index&controller=vacancies&only_path=true&search%5Bcategory_id%5D=38&type=vacancies']


# data = []
# for pg in quote_page:
#     # query the website and return the html to the variable ‘page’
#     page = urlopen(pg)

# # parse the html using beautiful soap and store in variable `soup`
#     soup = BeautifulSoup(page, 'html.parser')

# # Take out the <div> of name and get its value
#     name_box = soup.find('h3', attrs={'class': 'results-i-title'})
#     name = name_box.text.strip()  # strip() is used to remove starting and trailing

# # get the index price
#     # price_box = soup.find(‘div’, attrs={‘class’: ’price’})
#     # price = price_box.text

# # save the data in tuple
#     data.append(name)
# print(data)
