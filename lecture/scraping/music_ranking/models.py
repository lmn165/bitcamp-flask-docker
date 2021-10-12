import pandas as pd
from bs4 import BeautifulSoup
import requests

from lecture.menu.models import menu2


# 파이썬에서 디폴트 생성자를 만든다 - __init__을 선언하지 않는다.
class MusicRanking(object):
    html = ''
    headers = {'User-Agent' : 'Mozilla/5.0'}
    class_name = []
    artists =[]
    titles = []
    dict = {}
    tag = ''
    fname = ''
    # 행렬 (dataframe)
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text

    def get_html(self):
        print(f'Crawling HTML is {self.html}')

    def get_raking(self):
        soup = BeautifulSoup(self.html, 'lxml')

        music_info = []

        for name in self.class_name:
            music_info.append(soup.find_all(name=f'{self.tag}', attrs={'class': f'{name}'}))
        _ = 0
        for title, artist in zip(*music_info):
            _ += 1
            print(f'{"*" * 50}\n{_} Rank\nTitle: {title.find("a").text}\nArtist: {artist.find("a").text}')
        self.class_name.clear()

    def insert_dict(self):
        # 방법 1
        # for i in range(0, len(self.tag)):
        #     self.dict[self.titles[i]] = self.artists[i]

        soup = BeautifulSoup(self.html, 'lxml')
        music_info = []
        for name in self.class_name:
            music_info.append(soup.find_all(name=f'{self.tag}', attrs={'class': f'{name}'}))
        for title, artist in zip(*music_info):
            # print(f'{"*" * 50}\n{_} Rank\nTitle: {title.find("a").text}\nArtist: {artist.find("a").text}')
            self.titles.append(title.find("a").text)
            self.artists.append(artist.find("a").text)
        # 방법 2
        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j

        self.class_name.clear()
        # 방법 3
        # for i, j in enumerate(self.titles):
        #     self.dict[j] = self.artists[i]

        print(dict)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path, sep='\t', na_rep='NaN')
