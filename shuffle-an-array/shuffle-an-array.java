class Solution {
    private int[] nums;
    private int[] nums1;
    private Random rand;
    
    // 
    public Solution(int[] nums) {
        this.nums=nums;
        this.nums1= nums.clone();
        rand=new Random();
        
    }
    
    public int[] reset() {
        return nums;
    }
    
    public int[] shuffle() {
        for(int i=0;i<nums1.length;i++){
            int j=i+rand.nextInt(nums1.length-i);
            int temp=nums1[i];
            nums1[i]=nums1[j];
            nums1[j]=temp;
        }
        return nums1;
}
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */