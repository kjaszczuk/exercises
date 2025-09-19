class Solution:
    def compress(self, chars: List[str]) -> int:
        if chars == []:
            return 0
        s = [chars[0]]
        counter = 0
        reversed_counter = []
        flag_append = False
        for i in range (len(chars)):
            if chars[i] == s[-1]:
                counter += 1
            if chars[i] != s[-1] or i == len(chars)-1:
                if chars[i] != s[-1]:
                    flag_append = True
                if counter > 1:
                    while counter != 0:
                        reversed_counter.append(counter%10)
                        counter //= 10
                    for j in range (len(reversed_counter)-1, -1, -1):
                        s.append(str(reversed_counter[j]))
                    reversed_counter = []
                counter = 1
                if flag_append:
                    s.append(chars[i])
                    flag_append = False
        for i in range (len(s)):
            chars[i] = str(s[i])
        return len(s)
# 37, 6
