class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """Runtime: 836 ms, faster than 80.80% of Python3 online submissions for Image Smoother.
        Memory Usage: 14.7 MB, less than 79.46% of Python3 online submissions for Image Smoother."""
        filt_img = []
        for i in range(len(img)):
            #add new row
            filt_img.append([])
            for j in range(len(img[0])):
                neighbors = 0
                mask = 0
                #iterate smoother rows
                for dx in range(-1,2):
                    #iterate smoother cols
                    for dy in range(-1,2):
                        #check if index exists
                        if 0<=i+dx<len(img) and 0<=j+dy<len(img[0]):
                            mask += img[i+dx][j+dy]
                            neighbors +=1
                #add smoothed value to end of list
                filt_img[-1].append(mask//neighbors)       
        return filt_img
                