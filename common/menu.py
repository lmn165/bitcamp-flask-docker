def print_menu(ls) -> int:
    str = ''
    for i, val in enumerate(ls):
        str += f'{i}-{val}\t'
    return int(input(str))
