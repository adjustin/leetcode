class Solution:
    def isHappy(self, n: int) -> bool:
        a=n
        list1=[]
        while(a!=1): 
            res = [int(x) for x in str(a)]
            a=0
            print(res)
            for i in res:
                a+=i*i
            print(a)
            if(a not in list1):
                list1.append(a)
            else:
                return 0
        return 1
        
            
            
            
        

        