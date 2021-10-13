import numbers
import string

import pandas as pd
from icecream import ic


class Conversion(object):
    def __init__(self):
        print('자료구조 타입변환 예제')
        print('Q1. 1부터 9까지 요소를 갖는 튜플 생성')
        tpl = self.create_tuple()
        ic(type(tpl))
        ic(tpl)
        print('Q2. 튜플을 리스트로 전환')
        lst = self.tuple_to_list(tpl)
        ic(type(lst))
        ic(lst)
        print('Q3. 리스트의 int 값을 float 로 전환')
        lst = self.int_to_float(lst)
        ic(type(lst))
        ic(lst)
        print('Q4. float 리스트를 int 리스트 로 전환')
        lst = self.float_to_int(lst)
        ic(type(lst))
        ic(lst)
        print('Q5. int 리스트를 딕셔너리로 전환. 단 키값은 int 를 str 로 변환시켜서 활용함')
        dic = self.list_to_dictionary(lst)
        ic(type(dic))
        ic(dic)
        print('Q6. "hello"를 가진 튜플생성')
        tpl = self.hello_to_tuple('hello')
        ic(type(tpl))
        ic(tpl)
        print('Q7. 6번 튜플을 리스트로 전환')
        lst = self.hello_to_list(tpl)
        ic(type(lst))
        ic(lst)
        print('Q8. 5번 딕셔너리를 dataframe 으로 전환, orient 속성값으로 인덱스 지정')
        df = self.dictionary_to_dataframe(dic)
        ic(type(df))
        ic(df)
        print('Q9. 1번 튜플의 제곱을 요소로 갖는 리스트 출력')
        lst = self.tuple_square(self.create_tuple())
        ic(type(lst))
        ic(lst)
        print('Q10. 구구단 한 줄 출력 2*1=2, 2*2=4, ..., 9*9=81')
        lst = self.gugudan(self.create_tuple())
        ic(type(lst))
        ic(lst)
        print('Q11. 1번 튜플에서 3의 배수만 문자열로 갖는 리스트 출력')
        lst = self.three_multi_change_str(self.create_tuple())
        ic(type(lst))
        ic(lst)
        print("Q12. 키는 a, b, c 이고 값은 [1, 2, 3], [4, 5, 6], [7, 8, 9] 인 딕셔너리 출력")
        dt = self.abc_dict()
        ic(type(dt))
        ic(dt)
        print("Q13. 12번 딕셔너리에서 키값을 인덱스로 갖는 데이터프레임 출력")
        df = self.orient_index(dt)
        ic(type(df))
        ic(df)
        print("Q14. 12번 딕셔너리에서 키값을 컬럼으로 갖는 데이터프레임 출력")
        df = self.orient_column(dt)
        ic(type(df))
        ic(df)

    def create_tuple(self) -> ():
        return (1, 2, 3, 4, 5, 6, 7, 8, 9)

    def tuple_to_list(self, tpl) -> []:
        return [i for i in tpl]

    def int_to_float(self, lst) -> []:
        # m = map(float, lst)
        # ic(type(m))
        # ic(list(m))
        return [float(i) for i in lst]

    def float_to_int(self, lst) -> []:
        return [int(i) for i in lst]

    def list_to_dictionary(self, lst) -> {}:
        return {str(i): i for i in lst}

    def hello_to_tuple(self, payload: str) -> ():
        return tuple(i for i in payload)

    def hello_to_list(self, tpl) -> []:
        return [i for i in tpl]

    def dictionary_to_dataframe(self, dic) -> object:
        return pd.DataFrame.from_dict(dic, orient='index')

    def mypow(self, x):
        return pow(x, 2)

    def tuple_square(self, tpl) -> []:
        # return [i ** 2 for i in tpl]
        # return list(map(self.mypow, tpl))
        return list(map(lambda x: pow(x, 2), tpl))

    # print('Q10. 구구단 한 줄 출력 2*1=2, 2*2=4, ..., 9*9=81')
    def gugudan(self, tpl) -> [[]]:
        # return list(map(lambda x: [x * i for i in range(2, 10)], tpl))
        return list(map(lambda x: list(map(lambda y: f'{x} * {y} = {x*y}', range(2, 10))), tpl))

    # print('Q11. 1번 튜플에서 3의 배수만 문자열로 갖는 리스트 출력')
    def three_multi_change_str(self, tpl) ->[]:
        return list(map(lambda x: str(x) if x % 3 == 0 else x, tpl))

    def abc_dict(self):
        return {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}

    def orient_index(self, dt):
        return pd.DataFrame.from_dict(dt, orient='index')

    def orient_column(self, dt):
        return pd.DataFrame.from_dict(dt)

if __name__ == '__main__':
    Conversion()
