class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        list1=[1]*n
        list1[0]=1
        list2=[1]*n
        list2[n-1]=1
        list3=[0]*n
        
        a=1
        for i in range(1,n):
            a*=nums[i-1]
            list1[i]=a    
        a=1
        for i in range(n-2,-1,-1):
            a*=nums[i+1]
            list2[i]=a    
            
        for i in range(n):
            list3[i]=list1[i]*list2[i]
        return list3
        