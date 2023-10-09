/* 
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/836/
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

"2 + 8 - 6 * 2 / 3 / 7 - 8"

    -
   / \  
  +   6
 / \
2   8
                   -
          /                 \
         -                   8 
   /          \              
  +            *
 / \          / \  
2   8        6   // 
                 / \
                //  7
               / \
              2   3  
           
             
              
Iterate input string for elements
    If element is operator
       Iterate the right child till operator with greater precedence found or value node is found
        Then atach the found node to the left child and attach it to the parent of the found node.
    If element is value
        Goto right side of operator nodes till emplty slot is found in one of the operator node children, then add the node there.

Create stack st.
push top node to stack[which should always be operator node.]
Iterate till stack is empty
    currNode  = st.Pop();
    left = currNode.Left;
    right = currNode.Right;
    if any of the Left or right node is operator, then
        st.Push(curNode)
        if(Left node is operator)
            st.Push(Left)
        if(Right node is operator)
            st.Push(Right)
    else
        Perform currNode.Value operation on Left.Value and Right.Value
        if(currNode.Parent == null)
            return result;
        resultNode = new Node{Value = result, Parent = currNode.Parent, IsLeftChild = currNode.IsLeftChild};
        if(currNode.IsLeftChild){
            currNode.Parent.Left = resultNode;
        }
        else
        {
            currNode.Parent.Right = resultNode;
        }

"3+2*2"
" 3/2 "
*/
class Solution {
    

   public int Calculate(String s) {
        Node tree = null;
        StringBuilder currVal = new StringBuilder();
        foreach(char c in s){
            
            bool isOperator = IsOperator(c);
            if(isOperator){
                if(currVal.Length > 0){
                    tree = AddToTree(tree, currVal.ToString(), false);       
                    currVal.Clear();
                }
                tree = AddToTree(tree, c.ToString(), true);
            }
            else{
                if(c != ' '){
                    currVal.Append(c);
                }
                else if(currVal.Length > 0){
                    tree = AddToTree(tree, currVal.ToString(), false);       
                    currVal.Clear();
                }
            }
        }

        if(currVal.Length > 0){
            tree = AddToTree(tree, currVal.ToString(), false);       
            currVal.Clear();
        }
       
        Stack<Node> st = new();
        st.Push(tree);

        while(!(st.Count == 0)){
            Node currNode = st.Pop();
            //Console.WriteLine($"char : {currNode.Value}");
            //Console.WriteLine($"left : {currNode.Left.Value} ; right : {currNode.Right.Value} ");
            Node left = currNode.Left;
            Node right = currNode.Right;
            if(left == null && right == null){
                return Convert.ToInt32(currNode.Value);
            }
            if(left.IsOperator || right.IsOperator){
                st.Push(currNode);
                if(left.IsOperator)
                    st.Push(left);
                if(right.IsOperator)
                    st.Push(right);
            }
            else{
                int result = Operate(currNode.Value, left.Value, right.Value);
                //Console.WriteLine($"parent : {currNode.Parent}; {currNode.Value} ; {currNode.Left.Value} ; right : {currNode.Right.Value} ");
                if(currNode.Parent == null)
                    return result;
                Node resultNode = new Node{Value = Convert.ToString(result), Parent = currNode.Parent, IsLeftChild = currNode.IsLeftChild};
                AttachToParent(resultNode, currNode);
            }
        }

        throw new ArgumentException($"Invalid Expression : {s}");

    }

    private class Node{
        public string Value {get; set;}
        public Node Parent {get; set;}
        public Node Left {get; set;}
        public Node Right {get; set;}
        public bool IsOperator {get; set;}
        public bool IsLeftChild {get; set;}
    }

    Dictionary<string, int> _operatorPrecedence = new() {{"-",0}, {"+",0}, {"*",2}, {"/",2}};

    Node AddToTree(Node root, string value, bool isOperator){
        var node = new Node{Value = value, IsOperator = isOperator};
        if(root == null){
            root = node;
            return root;
        }
        Node currNode = root;
        if(isOperator){
            while(currNode!=null){
                if(currNode.IsOperator && _operatorPrecedence[currNode.Value] < _operatorPrecedence[node.Value]){
                    currNode = currNode.Right;
                }
                else{
                    if(currNode == root){
                        root = node;
                    }
                    else
                    {
                        node.Parent = currNode.Parent;
                        AttachToParent(node, currNode);
                    }
                    node.Left = currNode;
                    currNode.Parent = node;
                    currNode.IsLeftChild = true;
                    return root;
                }
            }
        }
        else{
            while(currNode.Right !=null){
                currNode = currNode.Right;
            }
            if(currNode.Left == null){
                currNode.Left = node;
                node.Parent = currNode;
                node.IsLeftChild = true;
            }
            else
            {
                currNode.Right = node;
                node.Parent = currNode;
                node.IsLeftChild = false;   
            }
        }    
        return root;
    }

 

    void AttachToParent(Node nodeToAttach, Node nodeToReplace){
         if(nodeToReplace.IsLeftChild){
            nodeToReplace.Parent.Left = nodeToAttach;
        }
        else
        {
            nodeToReplace.Parent.Right = nodeToAttach;
        }
    }

    bool IsOperator(char c){
        if(c == '+' || c == '*' || c == '/' || c == '-')
            return true;
        else return false;
    }

    int Operate(string op, string left, string right){
        switch(op){
            case "+": return Convert.ToInt32(left) + Convert.ToInt32(right);
            case "-": return Convert.ToInt32(left) - Convert.ToInt32(right);
            case "*": return Convert.ToInt32(left) * Convert.ToInt32(right);
            case "/": return Convert.ToInt32(left) / Convert.ToInt32(right);
            default : throw new ArgumentException($"Invalide Operator : {op}");
        }
    }
}

/* 3-1+2*3+1
 3-, currnum=3 lastnum = 0, lastsign = + -> result = 0, lastnum = 3, currnum = 0, lastsign = -
 3-1+, result = 0, lastnum = 3, currnum = 1, lastsign = - -> result = , lastnum = , currnum = , lastsign = 

*/
class Solution{
    public int Calculate(string s){
        int result = 0;
        int lastExpr = 0;
        int currNumber = 0;
        char lastOperation = '+';
        for(int i =0; i<s.Length; i++){
            char c = s[i];

            if(char.IsDigit(c)){
                currNumber = currNumber*10 + (c - '0');
                //Console.WriteLine(currNumber);
                
            }
            if((!char.IsDigit(c) && c!=' ') || (i == s.Length-1)){
                //Console.WriteLine($"i : {i}");
                if(lastOperation == '+' || lastOperation == '-'){
                    result += lastExpr;
                    lastExpr = (lastOperation == '+' ? currNumber : (-1)*currNumber);
                }
                else if(lastOperation == '*'){
                    lastExpr *= currNumber;
                }
                else if(lastOperation == '/'){
                    lastExpr /= currNumber;
                }
                if(i!= s.Length-1)
                    lastOperation = c;
                currNumber = 0;
            }
            
        }
        //Console.WriteLine($"result : {result} ;last : {lastExpr}; lastop : {lastOperation}");
        result += lastExpr;
        return result;
    }


}