class Palindrome(object):
    # def str_to_list(payload: str) -> []:
    #     strs = []
    #     for char in payload:
    #         if char.isalnum():
    #             strs.append(char.lower())
    #     return strs
    def str_to_list(self, payload: str) -> []:
        return [char.lower() for char in payload if char.isalnum()]

    def isPalindrome(self, ls: []) -> bool:
        # while len(ls) > 1:
            # if ls.pop(0) != ls.pop():
            #     return False
        return {"Result":False for i in ls if ls.pop(0) != ls.pop}


class ReverseString(object):
    def str_to_list(self, payload: str) -> []:
        return [i for i in payload]

    # def reverseString(ls: []):
    #     left, right =0, len(ls)-1
        # while left < right:
        #     ls[left], ls[right] = ls[right], ls[left]
        #     left += 1
        #     right -= 1
        # return ls

    def reverseString(self, ls: []):
        return [ls[i] for i in range(len(ls)-1, -1, -1)]

    def list_to_str(self, ls: []) -> []:
        return ''.join([i for i in ls])
