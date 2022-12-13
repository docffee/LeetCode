class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        a =[0,0]
        for st in students:
            a[st]+=1
        k = 0
        while k < len(sandwiches):
            if a[sandwiches[k]]>0:
                a[sandwiches[k]]-=1
            else:
                break
            k+=1
        return len(sandwiches)-k