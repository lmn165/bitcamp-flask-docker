from lecture.scraping.bugs_music.models import BugsMusic

if __name__ == '__main__':
    # 20210720
    # 16
    BugsMusic(
        f'https://music.bugs.co.kr/chart/track/realtime/total?chartdate={input("Date: ")}&charthour={input("Time: ")}').scrap()

