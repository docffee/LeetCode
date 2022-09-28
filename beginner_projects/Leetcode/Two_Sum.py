class Solution:
    def twoSum_brute(nums, target):
        # Double for loop. Brute force. O(n^2)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return([i,j])

    def twoSum_dict(nums, target):
        # Dictionary storage. O(n)
        seen = {}
        
        # enumerate gets index and value
        for i, num in enumerate(nums):
            if target - num in seen:
                return([seen[target - num], i])
            elif num not in seen:
                seen[num] = i

nums = [2,7,11,15]
target = 9

print(Solution.twoSum_brute(nums, target))

print(Solution.twoSum_dict(nums, target))