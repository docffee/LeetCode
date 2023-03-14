class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def main(a):
            if len(a) == len(nums):
                ans.append(a.copy())
                return
            else:
                for x in nums:
                    if x not in a:
                        a.append(x)
                        main(a)
                        a.pop()
        main([])
        return ans
