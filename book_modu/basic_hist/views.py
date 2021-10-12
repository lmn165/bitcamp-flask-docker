from book_modu.basic_hist.models import BasicHist

if __name__ == '__main__':
    basic_hist = BasicHist()

    # hist_show(get_dice(int(input(print('생성할 난수 갯수 입력: ')))))
    basic_hist.show_hist_about(basic_hist.highest_temperature(input(print('월을 입력해 주세요: '))), '08')