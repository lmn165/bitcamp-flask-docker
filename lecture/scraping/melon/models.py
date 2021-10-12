import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen


class MelonMusic:
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(urllib.request.Request(self.url, headers={'User-Agent' : 'Mozilla/5.0'})).read(), 'lxml')
        titles = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        artists = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        _ = 0
        for title, artist in zip(titles, artists):
            _ += 1
            print(f'{"*" * 50}\n{_} Rank\nTitle: {title.find("a").text}\nArtist: {artist.find("a").text}')

        # for i, title in enumerate(soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})):
        #     print(f'{"*" * 50}\n{str(i+1)} Rank\nTitle: {title.find("a").text}\nArtist: {artists[i].find("a").text}')



    '''
    def scrap(self):
        header = {'User-Agent' : 'Mozilla/5.0'}
        modi = urllib.request.Request(self.url, headers=header)
        soup = BeautifulSoup(urlopen(modi).read(), 'html.parser')
        ls_artist = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        for i, val in enumerate(soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})):
            print(f'{str(i+1)} Rank\nTitle: {val.find("a").text}\nArtist: {ls_artist[i].find("a").text}')

        # for i, val in enumerate(soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})):
        #     print(str(i+1) + ' Rank')
        #     print(f'Artist: {val.find("a").text}')

    '''
