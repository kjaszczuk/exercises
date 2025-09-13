class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
# misunderstood directions - not passing tests
        stack = []
        flag_append = False
        for i in asteroids:
            # add to stack if it's empty, or asteroids move in the same direction
            if not stack or stack[-1]*i > 0:
                stack.append(i)
            else:
                while stack or stack[-1]*i < 0:
                    if abs(stack[-1]) < abs(i):
                        stack.pop()
                        flag_append = True
                    elif stack[-1] == i*-1:
                        stack.pop()
                        flag_append = False
                        break
                    else:
                        flag_append = False
                        break
                if flag_append:
                    stack.append(i)
        return stack
