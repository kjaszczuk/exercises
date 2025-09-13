class Solution:
    def decodeString(self, s: str) -> str:
# working only for simplest case without nested brackets
        encoded = ""
        decoded = ""
        mult = 0
        for i in s:
            if i.isdigit():
                mult = int(i)
                continue
            elif i.isalpha():
                encoded += i
            elif i == ']':
                decoded += mult*encoded
                encoded = ""
        return decoded



