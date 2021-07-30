class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_string(self):
        print(f'\n안녕하세요, 제 이름은 {self.name} 이고, 나이는 {self.age}세 이고, {self.address}에서 거주합니다.')


def main():
    person = []
    persons = []
    while 1:
        menu = input('0-Exit 1-Add 2-Print\nChoose One Number')
        if menu == '1':
            persons.append(Person(input('name'), input('age'), input('address')))
        elif menu == '2':
            for i in persons:
                i.to_string()
        elif menu == '0':
            return


# 코드를 내부에서만 실행하기 위한 형태로 호출(외부에서 사용 불가!)
if __name__ == '__main__':
    main()