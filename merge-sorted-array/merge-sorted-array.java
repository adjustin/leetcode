class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int end=m+n-1;
        
        while(m-1>=0||n-1>=0){
            int x=m-1>=0? nums1[m-1]:Integer.MIN_VALUE;
            int y=n-1>=0? nums2[n-1]:Integer.MIN_VALUE;
            
            if(x>y){
                nums1[end--]=x;
                m--;
            }
            else{
                nums1[end--]=y;
                n--;
            }
        }
        
    }
}