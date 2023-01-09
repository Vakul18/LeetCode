/*https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
Attain max profit from stocks
{1,5,4,3,6}
*/
public class Solution{
	public int MaxProfit(int[] prices){
		int overallProfit = 0;
		int day = 0;
		int intermediateProfit = 0 - prices[0];
		for(int day=1; day<prices.Length;day++){
			if(prices[day-1]>prices[day]){
				if(intermediateProfit>0)
	 				overallProfit += intermediateProfit;
 				intermediateProfit = 0-prices[day];
			}
			else
			{
				intermediateProfit = intermediateProfit + prices[day];
			}
		}
		if(intermediateProfit>0)
	 		overallProfit += intermediateProfit;
		return overallProfit;
	}
}
