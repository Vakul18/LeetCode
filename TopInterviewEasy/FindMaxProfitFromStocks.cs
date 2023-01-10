/*https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
Attain max profit from stocks
{1,5,4,3,6} -> 7
{1,1,1} -> 0
{7,3,1,0} -> 0
{1,2,4,5} -> 4
*/
public class Solution{
	public int MaxProfit(int[] prices){
		int overallProfit = 0;
		int buyDay = 0;
        int day=1;
		for( ;day<prices.Length;day++){
			if(prices[day-1]>prices[day]){
 				overallProfit += prices[day-1]-prices[buyDay];
 				buyDay = day;
			}
		}
	 	overallProfit += prices[day-1]-prices[buyDay];
		return overallProfit;
	}
}

public class Solution{
	public int MaxProfit(int[] prices){
		int overallProfit = 0;
        	int day=1;
		for( ;day<prices.Length;day++){
			int profit = prices[day] - prices[day-1];
			if(profit>0){
				overallProfit += profit;
			}
			
		}
		return overallProfit;
	}
}
