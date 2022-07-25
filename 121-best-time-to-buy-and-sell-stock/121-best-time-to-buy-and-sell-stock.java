class Solution {
    public int maxProfit(int[] prices) {
        
        int min=prices[0];
        int max=0;
        
        for(int p: prices){
            if(p<min) min=p;
            max=Math.max(max,p-min);
        }
        return max;
        }
    }
    