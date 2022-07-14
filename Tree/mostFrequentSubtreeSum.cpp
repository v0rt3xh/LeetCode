/**
0508 Most Frequent Subtree Sum
DFS + count the frequency with a hash table.
 */
class Solution 
{
    unordered_map<int, int> frequency_counter;
    int maxFreq = 0;
public:
    vector<int> findFrequentTreeSum(TreeNode* root) 
    {
        getSum(root);
        vector<int> result; 
        for (auto &[sums, freq] : frequency_counter) 
        {
            if (freq == maxFreq) 
            {
                result.emplace_back(sums);
            }
        }
        return result;
        
    }
    
    int getSum(TreeNode *node) 
    {
        if (node == nullptr) 
        {
            return 0;
        }
        int current_Sum = getSum(node->left) + node->val + getSum(node->right);
        maxFreq = max(maxFreq, ++frequency_counter[current_Sum]);
        return current_Sum;
    }
};