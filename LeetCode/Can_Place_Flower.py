class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Runtime 164 ms Beats 92.28% Memory 14.3 MB Beats 72.67%
        zeros, ans = 1, 0 
        for f in flowerbed:
            if f == 0: 
                zeros += 1
            else:
                ans += (zeros - 1) // 2
                zeros = 0
        return ans + zeros // 2 >= n 