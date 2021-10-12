from icecream import ic


class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_string(self):
        ic(f'\n안녕하세요, 제 이름은 {self.name} 이고, 나이는 {self.age}세 이고, {self.address}에서 거주합니다.')