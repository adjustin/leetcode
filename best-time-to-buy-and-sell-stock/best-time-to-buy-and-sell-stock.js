/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {

        let min=prices[0];
        let maxProfit=0;
        
        for(let currentPrice of prices){
            min=Math.min(min,currentPrice);
            maxProfit=Math.max(maxProfit,currentPrice-min);
        }
        return maxProfit;

    }

