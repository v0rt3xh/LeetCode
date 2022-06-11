/**
0331 Verify Preorder Serialization of a Binary Tree
Introduce candidate slots.
Use a stack, the element of stack: 
    remaining slots following that node
    If we meet a '#', stack top element - 1.
    If we meet a non-empty element, stack top element - 1
    And push a '2' into the stack. 
    If the element turns to 0, pop it.
    Not enough slot -> return false during the process
    Remain slot after iteration -> return false
*/
class Solution 
{
public:
    bool isValidSerialization(string preorder) 
    {
        int N = preorder.length();
        int i = 0; // cursor
        stack<int> slot_stack;
        slot_stack.push(1);
        while (i < N) 
        {
            if (slot_stack.empty()) 
            {
                return false;
            }
            if (preorder[i] == ',') 
            {
                i++;
            } else if (preorder[i] == '#')
            {
                slot_stack.top() -= 1;
                if (slot_stack.top() == 0) 
                {
                    slot_stack.pop();
                }
                i++;
            } else 
            {
                while (i < N && preorder[i] != ',') 
                {
                    i++;
                }
                slot_stack.top() -= 1;
                if (slot_stack.top() == 0) 
                {
                    slot_stack.pop();
                }
                slot_stack.push(2);
            }
        }
        return slot_stack.empty();
    }
};

// improved version
class Solution2 {
public:
    bool isValidSerialization(string preorder) {
        int n = preorder.length();
        int i = 0;
        int slots = 1;
        while (i < n) {
            if (slots == 0) {
                return false;
            }
            if (preorder[i] == ',') {
                i++;
            } else if (preorder[i] == '#'){
                slots--;
                i++;
            } else {
                // Read the number
                while (i < n && preorder[i] != ',') {
                    i++;
                }
                slots++; // slots = slots - 1 + 2
            }
        }
        return slots == 0;
    }
};

