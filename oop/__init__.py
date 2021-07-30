if __name__ == '__main__':
    ls = ['Exit', '등록', '조회', '삭제']
    str = ''
    for i, val in enumerate(ls):
        str += f'{i}-{val} '
        # str += f'-{i} '.join(ls)
        # print(' '.join(ls))
    print(str)


    # str = enumerate(ls)
    # for i in str:
    #     print(i)