class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        #new_arr = []
        #new_arr[0] = max(arr)
        for i in range(len(arr)-1): 
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        
        return arr