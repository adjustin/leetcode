class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in nums:
            if i :
                nums[count]=i
                count+=1
        while(count<len(nums)):
            nums[count]=0
            count+=1
                

                