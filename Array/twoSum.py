'''
    001 Two Sum
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Key: the value of an integer
        # value: index
        # Basic idea -> 
        # We maintain a hashset.
        # We loop through the integer lsit
        # if its complementary part is in the dictionary as a key
        # we just return the correpsonding two index
        # otherwise add the term into the hashset.
        tool_dict = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in tool_dict.keys():
                return [i, tool_dict[target - nums[i]]]
            else:
                tool_dict[nums[i]] = i


