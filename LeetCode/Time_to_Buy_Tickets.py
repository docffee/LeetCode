class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """Runtime 67 ms Beats 40.37% Memory 13.8 MB Beats 65.12%"""
        time = 0 
        i = 0
        while tickets[k] != 0:
            if tickets[i] != 0: 
                tickets[i] -= 1
                time += 1 
            i = (i + 1) % len(tickets) 
        return time