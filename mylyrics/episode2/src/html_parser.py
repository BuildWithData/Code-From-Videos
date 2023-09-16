from bs4 import BeautifulSoup


PATH = "./../lyrics.html"


with open(PATH, "r") as f:
    html = f.read()

dom = BeautifulSoup(html, "html.parser")
