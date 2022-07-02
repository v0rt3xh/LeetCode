/**
0383 Ransom Note
Hashmap (use array instead here.)
Key point:
Early termination when < 0 appear in the hash map.
*/
class Solution 
{
public:
    bool canConstruct(string ransomNote, string magazine) 
    {
        if (ransomNote.size() > magazine.size()) 
        {
            return false;
        }
        vector<int> hashMap(26);
        for (auto &c_mag : magazine) 
        {
            hashMap[c_mag - 'a']++;
        }
        for (auto &c_note : ransomNote) 
        {
            hashMap[c_note - 'a']--;
            if (hashMap[c_note - 'a'] < 0) 
            {
                return false;
            }
        }
        return true;
        
    }
};