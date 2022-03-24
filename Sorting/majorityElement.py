'''
0169 Majority Element
O_o, That 'voting' algorithm.
Boyer-Moore Algorithm
The majority element gets half of the votes,
If we count majority element's vote as 1
other element's votes as -1
The overall sum shuold be >= 0
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 1
        candidate = nums[0]
        # We can just for num in nums though
        # don't have to start from index 1
        for i in range(1, len(nums)):
            if candidate != nums[i]:
                if votes == 0:
                    # swap candidate
                    candidate = nums[i]
                    votes += 1
                else:
                    # reduce votes, if current votes > 0
                    votes -= 1
            else:
                votes += 1
        return candidate

# Other approach:
# hash table
# sorting