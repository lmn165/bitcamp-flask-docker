'''
name, phone, email, address
'''


class Contacts:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        print(f'{self.name}, {self.phone}, {self.email}, {self.address}')


def set_contact() -> object:
    return Contacts(input('name: '), input('phone: '), input('email: '), input('address: '))


def get_contact(ls):
    for i in ls:
        i.to_string()


def del_contact(contacts, name):
    for i, val in enumerate(contacts):
        if name == val.name:
            del contacts[i]
            # contacts.pop(i)
            break


def menu1(ls) -> int:
    return int(input('\t'.join(ls)))


def menu2(ls) -> int:
    str = ''
    # '+=' 연산자는 두 문자열을 만들고 새로운 메모리에 저장하며,
    # 기존 문자열의 참조를 변경하는 연산을 반복적으로 수행하므로 .join 메소드에 비해 성능이 떨어진다.
    for i, val in enumerate(ls):
        str += f'{i}-{val}\t'
    return int(input(str))


def main():
    ls = []
    # c = Contacts()
    while 1:
        menu = menu2(['Exit', '등록', '조회', '삭제'])
        if menu == 0: return
        elif menu == 1:
            t = set_contact()
            ls.append(t)
            pass
        elif menu == 2:
            get_contact(ls)
        elif menu == 3:
            del_contact(ls, input('del_name: '))
        else: break


if __name__ == '__main__':
    main()