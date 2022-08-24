/**
0638 Shopping Offers
DFS + Memoization
State: Those needs (Has to be length n)
Preprocess: remove dumb specials (not saving our money)
DFS syntax (price, needsState, specials, n)
Only when not in memo, we start the dfs step.
    - First compute the cost of direct purchase / not using specials
    - Then, try using special.
    - maintain a next-needsState array, if (combo[item] > needs[item]),
      do not purchase (do not emplace to the array).
    - Only when needsState array has a length of n, we start recursion.
*/

class Solution 
{
public:
    map<vector<int>, int> memo; 
    
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) 
    {
        // We first rule out those 'useless' special combo.
        // Higher price than direct purchase.
        int num = price.size();
        
        vector<vector<int>> filterSpecial;
        for (auto& element: special) 
        {
            int totalCount = 0, totalPrice = 0;
            for (int i = 0; i < num; i++) 
            {
                totalCount += element[i];
                totalPrice += price[i] * element[i];
            }
            if (totalCount > 0 && totalPrice > element[num]) 
            {
                filterSpecial.emplace_back(element);
            }
        }
        return dfs(price, needs, filterSpecial, num);
    }
    
    int dfs(vector<int> price, vector<int> curNeeds, vector<vector<int>>& filterSpecial, int num) 
    {
        if (!memo.count(curNeeds)) 
        {
            int minPrice = 0;
            // Directly Purchase
            for (int i = 0; i < num; i++) 
            {
                minPrice += price[i] * curNeeds[i];
            }
            for (auto& curSpecial : filterSpecial) 
            {
                int specialPrice = curSpecial[num];
                vector<int> nextNeeds;
                for (int i = 0; i < num; i++) 
                {
                    if (curNeeds[i] < curSpecial[i]) 
                    {
                        break; // Cannot purchase redundant items
                    }
                    nextNeeds.emplace_back(curNeeds[i] - curSpecial[i]);
                }
                if (nextNeeds.size() == num) 
                {
                    // We can buy the combo
                    minPrice = min(minPrice, dfs(price, nextNeeds, filterSpecial, num) + specialPrice);
                }
                
            }
            memo[curNeeds] = minPrice;
        }
        return memo[curNeeds];
    }
};