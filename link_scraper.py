from bs4 import BeautifulSoup
import requests

class Link:
    def __init__(self, link):
        self.link = link

    def get_link(self):
        return self.link

    def scraping_link(self):
        try:
            r = requests.get(self.link)
        
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')

                link_unique = set()
                num = 1

                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href not in link_unique:
                        print(f"{num}. {href}")
                        link_unique.add(href)
                        num += 1

        except:
            print(f"{self.link} Failed to resolved\n")

    def run(self):
        print(f"Domain: {self.get_link()}")
        self.scraping_link()

if __name__ == "__main__":

    link = Link("https://link.com")
    link.run()
