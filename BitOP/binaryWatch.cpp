/**
0401 Binary Watch
Nice watch, won't buy though
Enumerate by: hours in [0, 11], minutes in [0, 59]
*/
class Solution 
{
public:
    vector<string> readBinaryWatch(int turnedOn) 
    {
        vector<string> result;
        for (int hour = 0; hour < 12; hour++) 
        {
            for (int minute = 0; minute < 60; minute++) 
            {
                if(__builtin_popcount(hour) + __builtin_popcount(minute) == turnedOn)
                {
                    result.push_back(to_string(hour) + ":" + (minute < 10 ? "0" : "") + to_string(minute));
                }
            }
        }
        return result;
    }
};