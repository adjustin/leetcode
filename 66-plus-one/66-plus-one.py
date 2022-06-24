class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=""
        result=[]
        for digit in digits:
            a+=str(digit)
        for i in str(int(a)+1):
            result.append(int(i))
        return result
              
