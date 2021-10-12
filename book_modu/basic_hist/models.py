import matplotlib.pyplot as plt
import random

from book_modu.changed_temperatures_on_my_birthday.models import ChangedTemperaturesOnMyBirthday


class BasicHist(object):
    def hist_show(self, dice: []):
        plt.hist(dice)
        plt.show()

    def get_dice(self, bins: int) -> []:
        ls = []
        [ls.append(random.randint(1, 6)) for i in range(5)]
        return ls
        # return [random.randint(1, 6) for i in range(bins)]

    def highest_temperature(self, month: str) -> []:
        birth = ChangedTemperaturesOnMyBirthday()
        birth.read_data()
        arr = [float(i[-1]) for i in birth.data if i[-1] != '' if i[0].split('-')[1] != month.rjust(2, '0')]
        # arr = []
        # for i in birth.data:
        #     if i[-1] != '':
        #         if i[0].split('-')[1] != month.rjust(2, '0'):
        #             arr.append(float(i[-1]))
        return arr

    def show_hist_about(self, arr: [], month: str):
        plt.hist(arr, bins=100, color='r', label=f'{month} Month')
        plt.legend()
        plt.show()
