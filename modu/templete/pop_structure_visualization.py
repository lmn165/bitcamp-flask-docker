import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd


class Population():
    data: [] = list()

    def read_data(self):
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간.csv', 'rt', encoding='UTF-8'))
        next(data)
        # print([i for i in data])
        self.data = data

    def pop_per_dong(self, dong: str) -> []:
        arr = []
        [arr.append(int(j)) for i in self.data if dong in i[0] for j in i[3:]]
        return arr

    def show_plot(self, arr: []):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()

    def numpy_pop_per_dong(self, dong: str) -> []:
        arr = []
        data = list(1)
        for i in data:
            if dong in i[0]:
                arr = np.array(i[3:], dtype=int) / int(i[2].replace(',', ''))

        for i in data:
            np.array(i[3:], dtype=int)
            # away =  / int(i[2].replace(',', ''))
            # print(arr - away)
        # tmp = []
        # [a.append(np.array(i[3:], dtype=int)) for i in self.data if dong in i[0]]
        # print(tmp)
        print(arr)
        # return arr

    def find_similar_pop_structure(self, name):
        pass


if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    # pop.show_plot(pop.pop_per_dong('월계3동'))
    pop.numpy_pop_per_dong('양재1동')
    # pop.find_similar_pop_structure(input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요: '))