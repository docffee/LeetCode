class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Runtime 71ms 8.20% Memory Usage 13.78 MB 59.64%
        num_jewels = 0
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    num_jewels += 1
        return num_jewels

    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        # Runtime 61 ms 32.72% Memory Usage 13.9 MB 11.99%
        return sum(s in jewels for s in stones)
        
    def numJewelsInStones3(self, jewels: str, stones: str) -> int:
        # Runtime 33 ms 93.08% Memory Usage 13.9 MB 11.99%
        return sum(map(jewels.count, stones))
