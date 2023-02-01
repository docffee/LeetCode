class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
       """Runtime 103 ms Beats 69.26% Memory 15.2 MB Beats 67.58%"""
       stack = []
       for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if a + stack[-1] < 0:
                        stack.pop()
                elif a + stack[-1] > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a: # if a is positive or negative append value
                    stack.append(a)
        return stack