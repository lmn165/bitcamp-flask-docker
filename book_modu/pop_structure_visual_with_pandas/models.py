import csv
import mypandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())


class Population():
    data: [] = list()
    arr: [] = list()
    result = []
    result_name = ''
    dong = ''

    def read_data(self):
        data = pd.read_csv('./data/202106_202106_연령별인구현황_월간.csv', index_col=0, encoding='UTF-8', thousands=',')
        data.to_csv('./data/202106_202106_연령별인구현황_월간_without_comma.csv', sep=',', na_rep='NaN')
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간_without_comma.csv', 'rt', encoding='UTF-8'))
        # print(data)
        next(data)
        self.data = list(data)

    def show_plot(self):
        plt.style.use('ggplot')
        plt.figure(figsize=(10, 5), dpi=300)
        plt.title(self.dong + ' 지역과 가장 비슷한 인구 구조를 가진 지역')
        plt.plot(self.arr, 'r', label=self.dong)
        plt.plot(self.result, 'b', label=self.result_name)
        plt.legend()
        plt.show()

    def pop_per_dong(self, dong: str) -> []:
        self.dong = dong
        min = 1
        # home = [int(j)/int(i[2]) for i in self.data if dong in i[0] for j in i[3:]]
        # self.arr = self.list_to_array(home)
        # print(self.arr)
        for i in self.data:
            if dong in i[0]:
                self.arr = np.array(i[3:], dtype=int) / int(i[2])
        # print(f'arr 타입: {type(self.arr)}')
        # print(self.arr)

        for i in self.data:
            away = np.array(i[3:], dtype=int) / int(i[2])
            # print(away)
            # print(f'away 타입: {type(away)}')
            s = np.sum(abs(self.arr - away))
            # s = np.sum((self.arr - away)**2)
            if s < min and dong not in i[0]:
                min = s
                self.result_name = i[0]
                self.result = away

    def array_to_list(self, arr: object) -> []:
        return arr.to_list()

    def list_to_array(self, ls: []) -> object:
        return np.array(ls)


