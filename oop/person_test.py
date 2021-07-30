'''
이름, 나이, 주소를 입력받아서 자기 소개하는 프로그램을 작성하시오.
출력은 안녕하세요, 제 이름은 Tom 이고, 나이는 28세 이고, 서울에서 거주합니다. 로 됩니다.
'''
class PersonTest(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class PersonTestService(object):
    def __init__(self):
        self.persons = []

    def add_person(self, person):
        self.persons.append(person)

    def to_string(self):
        for i in self.persons:
            print(f'안녕하세요, 제 이름은 {i.name} 이고, 나이는 {i.age}세 이고, {i.address}에서 거주합니다.')

    @staticmethod
    def main():
        personService = PersonTestService()
        while 1:
            menu = input('0-종료, 1-정보입력, 2-정보 출력\n')
            if menu == '0':
                return
            elif menu == '1':
                personService.add_person(PersonTest(input(f'이름: '), input(f'나이: '), input(f'거주지: ')))
            elif menu == '2':
                personService.to_string()


PersonTestService.main()
