/*
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
 0 1  2  3 4 5 6 7
[1,3,-1,-3,5,3,6,7], 3 -> [3,3,5,5,6,7]

[0],
[1],
[1],[2]

[1],[2]  : [3]

[1],[2],[3]  : [3, 3]
[4]  : [3, 3, 5]
[4],[5]  : [3, 3, 5, 5]
[6]  : [3, 3, 5, 5, 6]
[7] : [3, 3, 5, 5, 6, 7]

[7,2,4], 3 -> [7,4]

[0]
[0],[1]


[0],[1] : [7]

[2] : [7,4]



*/

public class Solution {

    class Node{
        public int Index {get; set;}
        public Node Prev {get; set;}
        public Node Next {get; set;}
    }

    public int[] MaxSlidingWindow(int[] nums, int k) {
        int n = nums.Length;
        var result = new List<int>(n-k+1);
        Node head = null;
        Node rear = null;
        int i;
        for(i = 0; i < k; i++){
            Node currNode = rear;
            while(currNode != null && nums[i] > nums[currNode.Index]){
                currNode = currNode.Prev;
                if(currNode != null){
                    currNode.Next = null;
                    rear = currNode;
                }
                else{
                    rear = null;
                    head = null;
                }
            }

            Node node  = new Node{Index = i}; 
            if(rear == null){
                head = node; 
                rear = node;
            }
            else{
                rear.Next = node;
                node.Prev = rear;
                rear = node;          
            }
        }

        print(head);
        if(head!=null)
            result.Add(nums[head.Index]);

        for(; i < n; i++){
            Console.WriteLine($"i : {i}");
            Node currNode = head;
            while(currNode!=null && currNode.Index <= (i-k))
            {
                currNode = currNode.Next;
            }

            head = currNode;
    
            if(currNode == rear || currNode == null){
                rear = currNode;
            }
            if(currNode != null){
                currNode.Prev = null;
            }
            Console.WriteLine("After pruning:");
            print(head);
            currNode = rear;
            while(currNode != null && nums[i] > nums[currNode.Index]){
                Console.WriteLine("Enter final:");
                currNode = currNode.Prev;
                if(currNode != null){
                    Console.WriteLine("Enter 1:");
                    currNode.Next = null;
                    rear = currNode;
                }
                else{
                    Console.WriteLine("Enter 2:");
                    rear = null; 
                    head = null;
                }
            }
            Console.WriteLine("PreFinal:");
            print(head);
            Node node  = new Node{Index = i}; 
            if(rear == null){
                head = rear = node;
            }
            else{
                rear.Next = node;
                node.Prev = rear;
                rear = node;          
            }
            Console.WriteLine("Final:");
            print(head);
            result.Add(nums[head.Index]);
        }

        return result.ToArray();
    }
    
    private void print(Node head){
        Node currNode = head;
        while(currNode!= null){
            Console.WriteLine($"{currNode.Index} -");
            currNode = currNode.Next;
        }
    }
}