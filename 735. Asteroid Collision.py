class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        flag_append = False
        for i in asteroids:
            # add to stack if it's empty, or asteroids move in the same direction
            if not stack or stack[-1]*i > 0 or (stack[-1] < 0 and i > 0):
                stack.append(i)
            else:
                while stack and (stack[-1]*i < 0 or (stack[-1] > 0 and i < 0)):
                    if stack[-1] < i*-1: # faster than abs (with abs it was 59,19)
                        stack.pop()
                        flag_append = True
                        continue
                    elif stack[-1] == i*-1:
                        stack.pop()
                        flag_append = False
                    elif stack[-1] == i:
                        flag_append = True
                    else:
                        flag_append = False
                    break
                if flag_append:
                    stack.append(i)
        return stack
# 94, 19
