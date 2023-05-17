import requests
import re
from bs4 import BeautifulSoup
import json

def web_request(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return ""

class Company:
    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url
    def gather_tech(self) -> None:
        self.technologies = []
        soup = BeautifulSoup(web_request(self.url), features="html.parser")
        text_body = str(soup.find("div", {"class": "subpage-description"}))
        search = [x[-1] for x in technologies_pattern.findall(text_body.lower())]
        if search:
            self.technologies = list(set(search))
    def __str__(self):
        return f"{self.name} {self.url} {self.technologies}"

technologies = [ "python", "django", "php", "laravel",
                 "c\#", "\.net", "asp.net", "c\+\+", "html", "css",
                 "javascript", "typescript", "java", "sql",
                 "angular", "react", "golang", "scala", "unity",
                 "docker", "lua" ]

technologies_pattern = re.compile(f"( |>)({'|'.join(technologies)})", flags=re.I)

def parse_link(raw: str) -> Company:
    name = re.search("\">.*\<\/a", raw).group(0)[2:-3]
    link = re.search("\".*\"", raw).group(0)[1:-1]
    return Company(name, link)

if __name__ == "__main__":
    BASE_URL = "https://www.inf.elte.hu/bsc-kepzes/szakmai-gyakorlati-helyek"

    soup = BeautifulSoup(web_request(BASE_URL), features="html.parser")
    container_ul = soup.find_all("ul")[-2]
    links = list(container_ul.findChildren("a", recursive=True))
    companies = [parse_link(str(l)) for l in links][:10]
    [c.gather_tech() for c in companies]
    print(json.dumps([c.__dict__ for c in companies]))

