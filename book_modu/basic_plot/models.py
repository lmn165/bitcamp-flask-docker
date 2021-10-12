import matplotlib.pyplot as plt


class BasicPlot(object):

    '''
    list 값은 y축이고, x축은 0부터 1까지 자동으로 증가한다.
    '''
    def plot_show(self):
        plt.title("legend")
        plt.plot([10, 20, 30, 40])
        plt.show()

    '''
    첫번째 list 가 x 축이고, 두번째 list 가 y 축이다.
    '''
    def plot_two_list_show(self):
        plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
        plt.show()

    '''
    그래프에 범례 넣기
    '''
    def plot_legend(self):
        plt.title("legend")
        plt.plot([10, 20, 30, 40], label='asc')
        plt.plot([40, 30, 20, 40], label='desc')
        plt.legend()
        plt.show()

    '''
    그래프에 선 색 변경
    '''
    def plot_color(self):
        plt.title("color")
        plt.plot([10, 20, 30, 40], color='skyblue', label='skyblue')
        plt.plot([40, 30, 20, 10], 'pink', label='desc')
        plt.legend()
        plt.show()

    '''
    그래프에 선 모양 바꾸기
    '''
    def plot_linestyle(self):
        plt.title("linestyle")
        plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='dashed')
        plt.plot([40, 30, 20, 10], color='b', linestyle=':', label='dotted')
        plt.legend()
        plt.show()

    '''
    그래프에 마커 모양 바꾸기
    '''
    def plot_scatter(self):
        plt.title("marker")
        plt.plot([10, 20, 30, 40], 'r.', label='circle')
        plt.plot([40, 30, 20, 10], 'b^', label='triangle up')
        plt.legend()
        plt.show()

# 꺾은 선 그래프 - deflected plot