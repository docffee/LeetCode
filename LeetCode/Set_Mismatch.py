class Solution:
    def findErrorNums1(self, nums):
        n = len(nums)
        s = n*(n+1)//2
        miss = s - sum(set(nums))
        duplicate = sum(nums) + miss - s
        return [duplicate, miss]

    def findErrorNums2(self, nums: List[int]) -> List[int]:
        # incomplete solution
        comp = list(range(1,len(nums)+1))
        print(set(nums) - set(comp))
        print(comp)
        count = nums[0]
        if nums[1] > nums[0] or nums[0] == 1:
            for n in nums:
                if n != count:
                    return [count-1, count]
                count+=1
        else:
            for n in nums:
                if n != count:
                    return [n, n-1]
                count-=1
                
