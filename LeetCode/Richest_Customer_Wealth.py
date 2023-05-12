class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        high_val = 0
        for account in acounts:
            cur_sum = sum(account)
            if high_val < cur_sum:
                high_val = cur_sum

        return high_val