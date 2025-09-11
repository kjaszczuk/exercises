class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(ch):
            return ch in 'aeiou'

        sumv = 0
        for i in s[:k]:
            if is_vowel(i):
                sumv += 1
        max_sum = sumv
        for i in range (k, len(s)):
            if (is_vowel(s[i-k]) and not is_vowel(s[i])):
                sumv -= 1
            elif (not is_vowel(s[i-k]) and is_vowel(s[i])):
                sumv += 1
                if sumv > max_sum:
                    max_sum += 1
                    if max_sum == k:
                        return k
        return max_sum
        #  74, 97
