/**
0223 Rectangle Area
First compute intersection
Then remove it
*/
class Solution 
{
public:
    int intersection(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) 
    {
        if ((min (ax2, bx2) > max(ax1, bx1)) && (min (ay2, by2) > max(ay1, by1))) 
        {
            return (min(ay2, by2) - max(ay1, by1)) * (min(ax2, bx2) - max(ax1, bx1)); 
        } else 
        {
            return 0;
        }
    }
    int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) 
    {
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - intersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2);
    }
};