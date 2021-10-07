from book_modu.pop_structure_visualization.models import Population

if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    # pop.show_plot(pop.pop_per_dong('월계3동'))
    pop.numpy_pop_per_dong('양재1동')
    # pop.find_similar_pop_structure(input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요: '))