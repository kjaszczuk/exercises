class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        Vowels = ('a', 'e', 'i', 'o', 'u')
        sumv = 0
        for i in s[:k]:
            if i in Vowels:
                sumv += 1
        max_sum = sumv
        for i in range (k, len(s)):
            if (s[i-k] in Vowels and s[i] not in Vowels):
                sumv -= 1
            elif (s[i-k] not in Vowels and s[i] in Vowels):
                sumv += 1
                if sumv > max_sum:
                    max_sum += 1
                    if max_sum == k:
                        return k
        return max_sum
        #  47, 13
