class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        
        for i,v in enumerate(nums):
            re=target-v
            if re in seen:
                return [seen[re],i]
            seen[v]=i
                
        return []