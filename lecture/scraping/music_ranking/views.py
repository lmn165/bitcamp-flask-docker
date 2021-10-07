from lecture.menu.models import menu2
from lecture.scraping.music_ranking.models import MusicRanking


if __name__ == '__main__':
    # 20210720
    # 16
    mr = MusicRanking()
    while 1:
        menu = menu2(['exit', 'Bugs URL', 'Melon URL', 'Output', 'Print dict', 'Dict To Dataframe', 'Dataframe to CSV'])
        # 0- exit, 1- Bugs (URL), 2- Melon (URL) 3- output, 4-print dict,
        # 5-dict to dataframe, 6-df to csv
        if menu == 0:
            break
        elif menu == 1:
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = 'chartdate=20210721&charthour=15'
            mr.set_html()
        elif menu == 2:
            mr.domain = 'https://www.melon.com/chart/index.htm?'
            mr.query_string = 'dayTime=2021072115'
            mr.set_html()
        elif menu == 3:
            mr.get_html()
        elif menu == 4:
            site = int(input(f'1.벅스, 2.멜론'))
            if site == 1:
                mr.tag = 'p'
                mr.class_name.append('title')
                mr.class_name.append('artist')
                mr.get_raking()
            elif site == 2:
                mr.tag = 'div'
                mr.class_name.append('ellipsis rank01')
                mr.class_name.append('ellipsis rank02')
                mr.get_raking()
        elif menu == 5:
            site = int(input(f'1.벅스, 2.멜론'))
            if site == 1:
                mr.tag = 'p'
                mr.class_name.append('title')
                mr.class_name.append('artist')
                mr.insert_dict()
                mr.dict_to_dataframe()
            elif site == 2:
                mr.tag = 'div'
                mr.class_name.append('ellipsis rank01')
                mr.class_name.append('ellipsis rank02')
                mr.insert_dict()
                mr.dict_to_dataframe()
        elif menu == 6:
            mr.fname = input(f'파일명 입력: ')
            mr.df_to_csv()
