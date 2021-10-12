from book_algorithm_interview.chap_06_string.models import Palindrome, ReverseString
from icecream import ic

if __name__ == '__main__':
    isPalindrome = Palindrome()
    ls = isPalindrome.str_to_list('A man, a plan, a canal: Panama')
    ic(ls)
    ic(isPalindrome.isPalindrome(ls))

    reverse = ReverseString()
    ls = reverse.str_to_list('apple')
    re_ls = reverse.reverseString(ls)
    ic(reverse.list_to_str(re_ls))