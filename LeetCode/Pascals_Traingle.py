class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [] 
        # Build triangle element by element
        for i in range(numRows):
            temp = []   # temporary array for row construction
            for j in range[i+1]:
                # temporary array begins and ends with 1
                if j == 0 or j == i:
                    temp.append(1)  
                # middle of array performs pascals pattern
                else:
                    temp.append(triangle[i-1][j] + triangle[i-1][j-1])
            triangle.append(temp)   # append constructed array to triangle
        return triangle

        """
        # To print triangle in pyramid shape
        for i in range(numRows):
            for j in range(numRows-i-1):
                print(format(" ","<2"), end="")
            for j in range(i+1):
                print(format(triangle[i][j],"<3"),end=" ")
            print()
        """
