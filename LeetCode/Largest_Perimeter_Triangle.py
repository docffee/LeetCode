class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
   
        nums.sort()
        nums = nums[::-1]

        #iterate through sorted list to find largest triangle
        for i in range(len(nums)-2):
            #triangle pass cases
            #s1, s2, s3 = nums[i], nums[i+1], nums[i+2]
            #s1+s2 >s3 and s1+s3>s2 and s2+s3>s1
            if (nums[i] < nums[i+1] + nums[i+2]):
                return nums[i]+ nums[i+1]+ nums[i+2]

        return 0

    def largestPerimeterBubbleSort(self, nums: List[int]) -> int:
        #sort array to get largest nuymbers first
          # loop to access each array element
      for i in range(len(nums)):

        # loop to compare array elements
        for j in range(0, len(nums) - i - 1):

          # compare two adjacent elements
          # change > to < to sort in descending order
          if nums[j] < nums[j + 1]:

            # swapping elements if elements
            # are not in the intended order
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
        
        #iterate through sorted list to find largest triangle
        for i in range(len(nums)):
            
            s1, s2, s3 = nums[i], nums[i+1], nums[i+2]

            if (s1+s2 >s3 and s1+s3>s2 and s2+s3>s1):
                return s1+s2+s3

        return 0