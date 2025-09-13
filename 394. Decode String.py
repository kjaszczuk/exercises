class Solution:
    def decodeString(self, s: str) -> str:
        encoded = ""
        mult = ""
        stack = []
        for i in s:
            if i.isdigit():
                mult += i
            elif i.isalpha():
                encoded += i
            elif i == '[':
                stack.append(encoded)
                stack.append(mult)
                encoded = ""
                mult = ""
            elif i == ']':
                encoded = int(stack.pop()) * encoded
                encoded = stack.pop() + encoded
        return encoded
# 100, 84
