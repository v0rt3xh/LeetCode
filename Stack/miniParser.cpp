/**
0385 Mini Parser
Stack.
 */
class Solution 
{
public:
    NestedInteger deserialize(string s) 
    {
        // Special case
        if (s[0] != '[') 
        {
            return NestedInteger(stoi(s));
        }
        // Use stack to store NestedInteger objects.
        stack<NestedInteger> working_stack;
        bool isNegative = false; // Add negative sign indicator
        int number = 0;
        for (int i = 0; i < s.size(); i++) 
        {   
            char character = s[i];
            if (character == '-') 
            {
                // negative sign
                isNegative = true;
            }
            else if (isdigit(character)) 
            {
                // if is a digit, add to number
                number = number * 10 + character - '0';
            }
            else if (character == '[') 
            {
                // Need to create the NestedInteger empty object.
                working_stack.emplace(NestedInteger());
            }
            else if (character == ',' or character == ']') 
            {
                // Meet a comma or ], stop adding number
                // Append sign if needed
                if (isdigit(s[i - 1])) 
                {
                    if (isNegative) 
                    {
                        number *= -1;
                    }
                    working_stack.top().add(number);
                }
                // restore the number / sign indicator
                number = 0;
                isNegative = false;
                // if we meet ], stop adding element to the NestedInteger obj.
                if (character == ']' && working_stack.size() > 1) 
                {
                    NestedInteger nestedOne = working_stack.top();
                    working_stack.pop();
                    working_stack.top().add(nestedOne);
                }
            }    
        }
        return working_stack.top();
    }
};