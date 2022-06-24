class Solution {
    public void moveZeroes(int[] nums) {
        int count =0;
        for(int n:nums){
            if (n!=0){
                nums[count]=n;
                count++;}}
            
        while(count<nums.length){
            nums[count]=0;
            count++;
                                 }
    }
}