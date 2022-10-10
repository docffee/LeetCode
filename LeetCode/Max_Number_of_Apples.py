class Solution:
    def maxNumberOfApplesNumpy(self, weight: List[int]) -> int:
        import numpy as np
        # Runtime 451 ms 5.11% percentile
        weight_sorted = np.sort(weight) 
        print(weight_sorted)
        basket = 0
        i=0
        for apple in weight_sorted:
            basket = basket + apple
            if basket > 5000:
                break
            i+=1

        print(basket)
        return i
                
            