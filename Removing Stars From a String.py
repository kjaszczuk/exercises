class Solution:
    def removeStars(self, s: str) -> str:
        # i = 0
        # s = list(s)
        # while i < len(s):
        #     if s[i] == '*':
        #         del s[i-1:i+1]
        #         i -= 1
        #     else:
        #         i += 1
        # return ''.join(s)
        # 5%, 24%

        stack = []
        for i in s:
            if i == '*':
                stack.pop()
            else:
                # stack += i      # 19, 60
                stack.append(i) # 98, 24
        return ''.join(stack)

