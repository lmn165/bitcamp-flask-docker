from lecture.menu.models import menu2
from lecture.contacts.models import Contacts

if __name__ == '__main__':
    ls = []
    while 1:
        menu = menu2(['Exit', '등록', '조회', '삭제'])
        if menu == 1:
            t = Contacts.set_contact()
            ls.append(t)
        elif menu == 2:
            Contacts.get_contact(ls)
        elif menu == 3:
            Contacts.del_contact(ls, input('del_name: '))
        else:
            break