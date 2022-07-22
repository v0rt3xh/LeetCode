/**
0274 H-index
First sort,
then traverse reversely. 
citations[cursor] > index:
    index += 1: Since we find one more paper, 
               that have citations >= index + 1
    cursor -= 1
*/
class Solution 
{
public:
    int hIndex(vector<int>& citations) 
    {
        sort(citations.begin(), citations.end());
        int index = 0, cursor = citations.size() - 1;
        while(cursor > -1 && citations[cursor] > index) 
        {
            index++;
            cursor--;
        }
        return index;   
    }
};