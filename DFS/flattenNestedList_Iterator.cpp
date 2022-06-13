/**
0341 Flatten Nested List Iterator
Method 1
iterate through nestedList, 
store the element in an array,
then iterate.
 */

class NestedIterator 
{
private:
    vector<int> listValues; 
    vector<int>::iterator cursor; 
    
    void dfs(vector<NestedInteger> &nestedList) 
    {
        for (auto &nest: nestedList) 
        {
            if (nest.isInteger()) 
            {
                listValues.push_back(nest.getInteger());
            }
            dfs(nest.getList());
        }
    }
    
public:
    NestedIterator(vector<NestedInteger> &nestedList) 
    {
        dfs(nestedList);
        cursor = listValues.begin();
    }
    
    int next() 
    {
        return *cursor++;
    }
    
    bool hasNext() {
        return cursor != listValues.end();
    }
};

// credit  LeetCode-Solution CN
class NestedIterator2 {
private:
    // pair -> first element: current position
            // second element: check if we have reached the end.
    stack<pair<vector<NestedInteger>::iterator, vector<NestedInteger>::iterator>> stk;

public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        stk.emplace(nestedList.begin(), nestedList.end());
    }

    int next() {
        // return the current element, 
        // And move the cursor to next element
        return stk.top().first++->getInteger();
    }

    bool hasNext() {
        // empty stack just return false
        while (!stk.empty()) {
            auto &p = stk.top();
            if (p.first == p.second) { // Reach the end of current list. pop
                stk.pop();
                continue;
            }
            if (p.first->isInteger()) { // return true if we have more elements
                return true;
            }
            // Now, the element is a list!
            // push the next element into the stack.
            // and move forward the cursor p.
            auto &lst = p.first++->getList();
            stk.emplace(lst.begin(), lst.end());
        }
        return false;
    }
};
