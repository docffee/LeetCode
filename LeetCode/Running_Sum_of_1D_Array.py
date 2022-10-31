class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Runtime: 79 ms, faster than 49.05% of Python3 online submissions for Running Sum of 1d Array.
        Memory Usage: 14.1 MB, less than 27.69% of Python3 online submissions for Running Sum of 1d Array.
        """
        summ=0
        tmp=[]
        for i in range(len(nums)):
            summ = nums[i] + summ
            tmp.append(summ)
        return tmp
            
    def runningSum2(self, nums: List[int]) -> List[int]:
        tmp=[nums[0]]
        for i in range(1,len(nums)):
            tmp.append(nums[i] + tmp[i-1])
        return tmp
            
    def runningSum3(self, nums: List[int]) -> List[int]:
        """
        Runtime: 40 ms, faster than 95.09% of Python3 online submissions for Running Sum of 1d Array.
        Memory Usage: 14.1 MB, less than 72.83% of Python3 online submissions for Running Sum of 1d Array.
        """
        for i in range(1,len(nums)):
            nums[i]=nums[i] + nums[i-1]
        return nums