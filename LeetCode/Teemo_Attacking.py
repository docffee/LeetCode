class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        #Runtime 248 ms Beats 97.1% Memory 15.5 MB Beats 40.6%
        ans =0
        time=0
        for i in timeSeries:
            ans += i + duration - max(i, time)
            time = i + duration
        return ans
