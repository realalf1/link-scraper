from bs4 import BeautifulSoup
import requests

class Link:
    def __init__(self, link):
        self.link = link
    
    def get_link(self):
        return self.link

    def scraping_link(self):
        r = requests.get(self.link).text
        soup = BeautifulSoup(r, 'html.parser')

        link_unique = set()
        num = 1

        for link in soup.find_all('a'):
            href = link.get('href')
            if href not in link_unique:
                print(f"{num}. {href}")
                link_unique.add(href)
                num += 1

    def run(self):
        print(f"Link: {self.get_link()}")
        print("Scraping Link:")
        self.scraping_link()

if __name__ == "__main__":

    link = Link("your-link")
    link.run()
