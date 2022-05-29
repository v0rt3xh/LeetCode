/*
0189 Rotate Array
I used extra space O(N) for the first version.
The beauty of swapping.
Ref @ xingyze:
nums = "----->-->"; k =3
result = "-->----->";

reverse "----->-->" we can get "<--<-----"
reverse "<--" we can get "--><-----"
reverse "<-----" we can get "-->----->"
*/
class Solution {
public:
    // Helper method: reverse the given (sub)array
    void reverse(vector<int>& nums, int start, int end) {
        while (start < end) {
            swap(nums[start], nums[end]);
            start += 1;
            end -= 1;
        }
    }
    
    void rotate(vector<int>& nums, int k) {
        k %= nums.size(); // The index we split on.
        reverse(nums, 0, nums.size() - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.size() - 1);
    }
};
