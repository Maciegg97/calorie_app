from selectorlib import Extractor
import requests


class Temperature:
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
    }

    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'calorie_app/temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-").lower()
        self.city = city.replace(" ", "-").lower()

    def _base_url(self):
        url = self.base_url + self.country + '/' + self.city
        return url

    def _scrape(self):
        url = self._base_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.headers)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        scraped_content = self._scrape()
        temp = float(scraped_content['temp'].replace("°C", "").strip())
        return temp


temp = Temperature("Poland", "Warsaw")
print(temp.get())
