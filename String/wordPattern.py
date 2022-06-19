'''
0290 Word Pattern
Hashmaps
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        compare_map_p2s = dict()
        compare_map_s2p = dict()
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        for pattern_character, character in zip(pattern, s):
            if pattern_character not in compare_map_p2s and character not in compare_map_s2p:
                compare_map_p2s[pattern_character] = character
                compare_map_s2p[character] = pattern_character
                continue
            elif pattern_character in compare_map_p2s and character in compare_map_s2p:
                if character == compare_map_p2s[pattern_character]:
                    continue
            return False
        return True