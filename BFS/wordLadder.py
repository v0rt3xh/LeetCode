'''
0127 Word Ladder
Credit: liweiwei1419
'''
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:   
        # 1. Use a hashset to store all the words.
        word_set = set(wordList)
        # exclude some special cases.
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        # remove beginWord from considerations
        if beginWord in word_set:
            word_set.remove(beginWord)
        # bfs processing queue
        queue = deque()
        # Start from beginWord
        queue.append(beginWord)
        # Visited set
        visited = set(beginWord)
        
        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            # bfs, search all neighbors
            for i in range(current_size):
                word = queue.popleft()
                # Change string word to an array
                word_list = list(word)
                for j in range(word_len):
                    # record the original character
                    origin_char = word_list[j]
                    # shift - one step
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        # next possible word
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            # in the sequence, then extra work
                            if next_word == endWord:
                                # EndWord, return step + 1,
                                # as we need one step to leave the current step
                                return step + 1
                            if next_word not in visited:
                                # not visisted, becomes a neighbor
                                queue.append(next_word)
                                # also visited!
                                visited.add(next_word)
                    # restore the original character, 
                    # after the 26 characters' loop
                    word_list[j] = origin_char
            # End one level, step append 1
            step += 1
        return 0


'''
作者：liweiwei1419
链接：https://leetcode-cn.com/problems/word-ladder/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''