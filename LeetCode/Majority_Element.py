class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElementSlow(self, nums: List[int]) -> int:
        # Runtime: 169 ms 95.81% Memory Usage: 15.6 MB 34.56%
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] = 1
        return max(dict.keys(), key=dict.get)
        # List comprehension method
        # return max([max(dict.values()) for dict in number])