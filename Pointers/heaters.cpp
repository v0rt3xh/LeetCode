/**
0475 Heaters
Seems to be a classic greedy problem (signal tower)
Sort + Two pointers.
We first sort houses and heaters,
then we put cursor #1, i on houses,
cursor #2, j on heaters,
for each house, we want to find its closest heater.
INIT: starting distance as abs(houses[i] - heaters[j])
Greedy approach, only when next heater closer to current house,
we move cursor #2.
Got the minimum distance for a house, (take min)
update the minimum coverage / radius standard (take max)
*/
class Solution 
{
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) 
    {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        int result = 0;
        for (int i = 0, j = 0; i < houses.size(); i++) 
        {
            int current_distance = abs(houses[i] - heaters[j]);
            while (j < heaters.size() - 1 && abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1])) 
            {
                j++;
                current_distance = min(current_distance, abs(houses[i] - heaters[j]));
            }
            result = max(result, current_distance);
        }
        return result;
    }
};