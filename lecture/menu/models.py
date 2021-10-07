def menu1(ls) -> int:
    return int(input('\t'.join(ls)))


def menu2(ls) -> int:
    # '+=' 연산자는 두 문자열을 만들고 새로운 메모리에 저장하며,
    # 기존 문자열의 참조를 변경하는 연산을 반복적으로 수행하므로 .join 메소드에 비해 성능이 떨어진다.
    str = ''
    for i, val in enumerate(ls):
        str += f'{i}-{val}\t'
    return int(input(str))
