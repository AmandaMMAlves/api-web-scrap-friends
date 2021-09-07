from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_friends_episodes(season):
    url = "https://www.imdb.com/title/tt0108778/episodes?season=" + str(season)
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')


    titles = soup.findAll("a", attrs={"itemprop": "name"})
    descriptions = soup.findAll("div", attrs={"class": "item_description"})

    episodes = []

    for index, title in enumerate(titles):
        episode = {
            "episode_number": str(index + 1),
            "title": title.getText(),
            "description": ' '.join(descriptions[index].getText().split())             
        }
        episodes.append(episode)

    return episodes