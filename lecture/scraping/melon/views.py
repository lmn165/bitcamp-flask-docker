from lecture.scraping.melon.models import MelonMusic


if __name__ == '__main__':
    # 2021072016
    MelonMusic(f'https://www.melon.com/chart/index.htm?dayTime={input("Date: ")}').scrap()