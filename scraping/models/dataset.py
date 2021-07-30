from dataclasses import dataclass


@dataclass
class Dataset(object):
    html = str
    headers = {'User-Agent': 'Mozilla/5.0'}
    class_name = object
    artists = object
    titles = object
    dict = dict
    tag = str

    @property
    def html(self) -> str: return self._html
    @html.setter
    def html(self, html): self._html = html