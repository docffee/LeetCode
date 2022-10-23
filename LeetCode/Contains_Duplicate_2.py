class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Runtime: 769 ms 80.70% Memory Usage: 28.3 MB 14.07% 
        dict = {}
        j = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] +=1
                if i-j[nums[i]]<= k: #if match number subtract last number index
                    return True
            dict[nums[i]] = 1
            j[nums[i]] = i  #remember most recent instance number and index of number
        return False

    def containsNearbyDuplicateFast(self, nums, k):
        # Runtime: 636 ms 93.95% Memory Usage: 27.3 MB 53.65% 
        dic = {}
        for ind, key in enumerate(nums):
            if key in dic and ind - dic[key] <= k:
                return True
            dic[key] = ind
        return False