/**
0435 Non-overlapping Intervals
Sorting + Greedy
  -Sort on 'end's. 
   Then decide what intervals to select,
  -If not overlapped with current selection, 
   Replace current selection -> new interval.
Original length - selected number -> result;
*/

class Solution 
{
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) 
    {
        sort(intervals.begin(), intervals.end(), [](const auto& u, const auto& v) {
            return u[1] < v[1]; // Sort by right ends.
        });
        int total_length = intervals.size();
        int right_end = intervals[0][1]; // init
        int selected = 1;
        for (int i = 1; i < total_length; i++) 
        {
            if (intervals[i][0] >= right_end) 
            {   // Non overlap
                // Then update
                right_end = intervals[i][1];
                selected++;
            }
        }
        return total_length - selected;
    }
};