import csv
import matplotlib.pyplot as plt
'''
next() 는 두가지 포맷으로 사용된다
function 구조로 사용되면 header 만 리턴한다.
consumer 구조로 사용되면 data 에서 header 를 제거된다.

row[날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃)] 최고기온은 -1 이다.

data: [] = list() 는 list 타입의 data 를 list() 로 초기화 시키는 것이다.
단, 한 메소드 내에서만 사용하면 로컬에서 초기화한다. 예제는 다음과 같다.
data : [] = None
def save_highest_temperatures(self):
     data = list()
그러나, 여러 메소드에서 사용하면 필드에서 초기화한다. 예제는 다음과 같다. 
data : [] = list()
'''


class ChangedTemperaturesOnMyBirthday(object):
    data : []
    highest_temperature: [] = []
    lowest_temperature: [] = list()

    def processing(self):
        self.read_data()
        self.save_highest_temperature()
        self.visualize_data()

    def read_data(self):
        data = csv.reader(open('data/seoul.csv', 'r', encoding='UTF-8'))
        next(data)
        self.data = data
        # print([i for i in data])

    def save_highest_temperature(self):
        [self.extract_date_data(val) for val in self.data if val[-1] != '' and val[-2] != '']
        # [self.highest_temperature.append(float(i[-1])) for i in self.data if i[-1] != '']
        # print(f'총 {len(self.highest_temperature)} 개')
        # print(self.highest_temperature)

    def visualize_data(self):
        plt.rc('font', family='Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.title('내 생일의 기온 변화 그래프')
        plt.plot(self.highest_temperature, 'r', label='high')
        plt.plot(self.lowest_temperature, 'b', label='low')
        plt.legend()
        plt.show()

    def extract_date_data(self, val):
        date = val[0].split('-')
        if date[1] == '06' and date[2] == '16':
            if 1995 <= int(val[0].split('-')[0]):
                self.highest_temperature.append(float(val[-1]))
                self.lowest_temperature.append(float(val[-2]))
'''
#     def show_highest_temperature(self):
        # print([i[-1] for i in self.data])
        # return [i[-1] for i in self.data]

    def highest_temperatures_my_birthday(self):
        high = []
        low = []
        for i in self.data:
            if i[-1] != '' and i[-2] != '':
                if 1983 <= int(i[0].split('-')[0]):
                    if i[0].split('-')[1]=='02' and i[0].split('-')[2] == '14':
                        high.append(float(i[-1]))
                        low.append(float(i[-2]))
        plt.rc('font', family='Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.title('내 생일의 기온 변화 그래프')
        plt.plot(high, 'hotpink', label='high')
        plt.plot(low, 'skyblue', label='low')
        plt.legend()
        plt.show()
'''


if __name__ == '__main__':
    this = ChangedTemperaturesOnMyBirthday()
    this.processing()
    # this.read_data()
    # this.highest_temperatures_my_birthday()
