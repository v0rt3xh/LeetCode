/**
0093 Restore IP Address
Backtracking. 
*/

class Solution 
{
private:
    static constexpr int IP_COUNT = 4; // We need 
    vector<string> result; // Final result
    vector<int> ipElements; // store the result of each backtrack step

public:
    void dfs(const string& s, int ipIndex, int ipStart) 
    {
        if (ipIndex == IP_COUNT)
        {
            // If we also have traversed through the string, 
            // Append the result.
            if (ipStart == s.size()) 
            {
                string newIp;
                for (int i = 0; i < IP_COUNT; i++) 
                {
                    newIp += to_string(ipElements[i]);
                    if (i != IP_COUNT - 1) 
                    {
                        // Add dot if needed.
                        newIp += ".";
                    }
                }
                result.push_back(move(newIp));
            }
            return;
            
        }
        if (ipStart == s.size()) 
        {
            // We haven't found enough slices.
            return;
        }
        if (s[ipStart] == '0') 
        {
            ipElements[ipIndex] = 0;
            dfs(s, ipIndex + 1, ipStart + 1);
        }
        // Otherwise, it's just a normal case.
        int running_number = 0;
        for (int ipEnd = ipStart; ipEnd < s.size(); ipEnd++) 
        {
            running_number = 10 * running_number + (s[ipEnd] - '0');
            // We will rule out the case of 0, so > 0 would suffice the need.
            if (running_number > 0 && running_number <= 0xFF) 
            {
                ipElements[ipIndex] = running_number;
                dfs(s, ipIndex + 1, ipEnd + 1);
            }
            else 
            {
                // Otherwise, out of range, stop it.
                break;
            }
        }
    }
    
    vector<string> restoreIpAddresses(string s) 
    {
        ipElements.resize(IP_COUNT);
        dfs(s, 0, 0);
        return result;
    }
};