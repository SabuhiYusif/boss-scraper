from urllib.request import urlopen
from bs4 import BeautifulSoup


# First page of the boss.az IT category
main_page_link = 'https://boss.az/vacancies?action=index&controller=vacancies&only_path=true&search%5Bcategory_id%5D=38&type=vacancies'

# open url using urllib library
first_page = urlopen(main_page_link)

soup = BeautifulSoup(first_page, 'html.parser')

list_of_pages = soup.find_all('span', attrs={'class': 'page '})

# add number of pages link to the list
pages = []
pages.append(main_page_link)

for p in list_of_pages:
    link = p.find('a')
    pg2 = 'https://boss.az' + link['href']
    pages.append(pg2)



# this will return all the links which has the PROQRAM keyword in their title
def get_links(page_links, keyword):
    links = []
    for p_l in page_links:

        page = urlopen(p_l)
        soup = BeautifulSoup(page, 'html.parser')

        list_of_jobs = soup.find_all('div', attrs={'class': 'results-i'})

        for i in list_of_jobs:
            if i.text.__contains__(keyword):
                link = i.find('a', attrs={'class': 'results-i-link'})
                links.append('https://boss.az' + link['href'])

    return links



links = get_links(pages, "PROQRAM")

print(links)
