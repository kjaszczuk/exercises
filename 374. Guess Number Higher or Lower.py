# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # low = 1
        # n = n + 1
        # while True:
        #     num = (low + n)//2
        #     guess_result = guess(num)
        #     if guess_result == 0:
        #         return num
        #     if guess_result == -1:
        #         n = (low + n)//2
        #     if guess_result == 1:
        #         low = (low + n)//2
# 27, 29

        low, high = 1, n
        myguess = (1+n) >> 1
        while ((res := guess(myguess)) != 0):
            if res == -1:
                high = myguess - 1
            else:
                low = myguess + 1
            myguess = (low+high) >> 1
        return myguess
# 57, 29
