class Solution:
    def candy(self, ratings: List[int]) -> int:
        num_child = len(ratings)
        left_candies = [0] * num_child
        for i in range(num_child):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left_candies[i] = left_candies[i - 1] + 1
            else:
                left_candies[i] = 1
        result = 0
        right = 1
        for i in range(num_child - 1, -1, -1):
            if i < num_child - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            result += max(right, left_candies[i])
        return result