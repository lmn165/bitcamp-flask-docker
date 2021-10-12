import mypandas as pd


class OlympicMedals(object):

    def read_wiki(self) -> object:
        df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0, index_col=0)
        summer = df[1].iloc[:, :5]
        summer.columns = ['경기수', '금', '은', '동', '계']
        print(summer.sort_values('금', ascending=False))
