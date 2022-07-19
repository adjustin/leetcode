class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int end=m+n-1;
        while(m-1>=0 ||n-1>=0){
            int x= m-1>=0? nums1[m-1]:Integer.MIN_VALUE; 
            int y= n-1>=0? nums2[n-1]:Integer.MIN_VALUE;
            
            System.out.println(y);
            nums1[end]= x>y? x:y;
            if(x>y) m--;
            else n--;
            end--;
        }
        
    }
}