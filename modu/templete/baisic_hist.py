import matplotlib.pyplot as plt
import random

from modu.templete import ChangedTemperaturesOnMyBirthday


def hist_show(dice: []):
    plt.hist(dice)
    plt.show()


def get_dice(bins: int) -> []:
    ls = []
    [ls.append(random.randint(1, 6)) for i in range(5)]
    return ls
    # return [random.randint(1, 6) for i in range(bins)]


def highest_temperature(month: str) -> []:
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    arr = [float(i[-1]) for i in birth.data if i[-1] != '' if i[0].split('-')[1] != month.rjust(2, '0')]
    # arr = []
    # for i in birth.data:
    #     if i[-1] != '':
    #         if i[0].split('-')[1] != month.rjust(2, '0'):
    #             arr.append(float(i[-1]))
    return arr


def show_hist_about(arr: [], month: str):
    plt.hist(arr, bins=100, color='r', label=f'{month} Month')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # hist_show(get_dice(int(input(print('생성할 난수 갯수 입력: ')))))
    show_hist_about(highest_temperature(input(print('월을 입력해 주세요: '))), '08')