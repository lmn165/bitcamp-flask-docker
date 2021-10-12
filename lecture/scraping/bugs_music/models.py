from bs4 import BeautifulSoup
from urllib.request import urlopen
'''
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
'''


class BugsMusic(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url).read(), 'lxml')
        titles = soup.find_all(name='p', attrs={'class':'title'})
        artists = soup.find_all(name='p', attrs={'class':'artist'})
        _ = 0
        for title, artist in zip(titles, artists):
            _ += 1
            print(f'{"*" * 50}\n{_} Rank\nTitle: {title.find("a").text}\nArtist: {artist.find("a").text}')


        '''
        for i, val in enumerate(soup.find_all(name='p', attrs={'class':'title'})):
            print(str(i+1) + ' Rank')
            print('title: ' + val.find('a').text)
            print('Artist: ' + ls_artist[i].find('a').text)
        '''
