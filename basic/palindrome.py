from pprint import pprint
class Palindrome(object):
    # def str_to_list(payload: str) -> []:
    #     strs = []
    #     for char in payload:
    #         if char.isalnum():
    #             strs.append(char.lower())
    #     return strs
    def str_to_list(payload: str) -> []:
        return [char.lower() for char in payload if char.isalnum()]

    def isPalindrome(ls: []) -> bool:
        # while len(ls) > 1:
            # if ls.pop(0) != ls.pop():
            #     return False
        return {"Result":True for i in ls if ls.pop(0) != ls.pop}

