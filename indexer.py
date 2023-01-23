import requests
import re

def get_tag(tag: str, input: str) -> str:
    tags = []
    for line in input.split("\n"):
        if tag in line:
            tags.append(line)
    return tags

def parse_link(raw: str) -> (str, str):
    name = re.search("\">.*\<\/a", raw).group(0)[2:-3]
    link = re.search("\".*\"", raw).group(0)[1:-1]
    return name, link

if __name__ == "__main__":
    BASE_URL = "https://www.inf.elte.hu/bsc-kepzes/szakmai-gyakorlati-helyek"
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        response_text = response.text
        links = get_tag("<li><a", response_text)
        links = [parse_link(l) for l in links]
        for l in links:
            print(l)