/*
{1,0},1 -> {0,1}
{-1,2,3},1 -> {0,1} 
{1},1 -> {0}
*/

public class Solution {
	private class Element{
	public int Value {get; set;}
	public int Index {get;set;}
	public override string ToString(){ return Value.ToString();}
	}

	private void QuickSort(Element[] list,int start,int end){
		if(start>=end){
			return;
		}
		int pivot = (start+end)/2;
		int finalPivotPosition = AdjustList(list,start,end,pivot);
		QuickSort(list,start,finalPivotPosition-1);
		QuickSort(list,finalPivotPosition+1,end);
	}

	private int AdjustList(Element[] list,int start,int end,int pivot){
		int pivotValue = list[pivot].Value;
		Element temp = list[end];
		list[end] = list[pivot];
		list[pivot] = temp;
		
		int i = start;
		int pivotPosition = start;
		while(i<end){
			if(list[i].Value<pivotValue){
				temp = list[i];
				list[i] = list[pivotPosition];
				list[pivotPosition] = temp;
				pivotPosition++;
			}
			i++;
		}
		temp = list[end];
		list[end] = list[pivotPosition];
		list[pivotPosition] = temp;
        return pivotPosition;
	}

	public int[] TwoSum(int[] nums, int target) {

		Element[] list = new Element[nums.Length];
		for(int index=0;index<nums.Length;index++){
			list[index] = new Element(){ Value=nums[index],Index=index };
		}
		
		QuickSort(list,0,nums.Length-1);
		Console.WriteLine(String.Join<Element>(",",list));
		int i = 0 ;
		int j = nums.Length-1;
		while(i<j){
		    int sum = list[i].Value + list[j].Value;
		    if(sum==target){
		        break;
		    }
		    else if(sum<target){
		        i++;
		    }
		    else{
		        j--;
		    }            
		}
		
		return new int[]{list[i].Index,list[j].Index};
	}
    }


public class Solution {
	private class Element{
	public int Value {get; set;}
	public int Index {get;set;}
	public override string ToString(){ return Value.ToString();}
	}



	public int[] TwoSum(int[] nums, int target) {

		Element[] list = new Element[nums.Length];
		for(int index=0;index<nums.Length;index++){
			list[index] = new Element(){ Value=nums[index],Index=index };
		}
		
		Array.Sort(list,(x,y)=> x.Value-y.Value);
		//Console.WriteLine(String.Join<Element>(",",list));
		int i = 0 ;
		int j = nums.Length-1;
		while(i<j){
		    int sum = list[i].Value + list[j].Value;
		    if(sum==target){
		        break;
		    }
		    else if(sum<target){
		        i++;
		    }
		    else{
		        j--;
		    }            
		}
		
		return new int[]{list[i].Index,list[j].Index};
	}
    }




public class Solution {


	public int[] TwoSum(int[] nums, int target) {

		var dict = new Dictionary<int,int>();
		for(int index=0;index<nums.Length;index++){
			int num = nums[index];
			int targetNum = target-num;
			if(dict.ContainsKey(targetNum)){
				return new int[]{index,dict[targetNum]};
			}
			else
			{
				dict[num] = index;
			}
		}
				
		return new int[0];
	}
    }


