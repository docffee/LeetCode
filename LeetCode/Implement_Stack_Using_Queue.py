class MyStack:
    """Runtime 30 ms Beats 84.79% Memory 14 MB Beats 68.85%"""
    def __init__(self):
        self.q = collections.deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)

        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        

    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return not len(self.q)