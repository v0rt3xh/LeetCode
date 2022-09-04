/**
0071 Simplify Path
Cpp version
*/

class Solution 
{
public:
    string simplifyPath(string path) 
    {
        auto split = [](const string& s, char delim) -> vector<string> 
        {
            vector<string> ret;
            string cur;
            for (char c : s) 
            {
                if (c == delim) 
                {
                    ret.push_back(move(cur));
                    cur.clear();
                }
                else 
                {
                    cur += c;
                }
            }
            ret.push_back(move(cur));
            return ret;
        };
        vector<string> dirs = split(path, '/');
        vector<string> myStack;
        for (string& dir: dirs) 
        {
            if (dir == "..") 
            {
                if (!myStack.empty()) 
                {
                    myStack.pop_back();
                }
            }
            else if (!dir.empty() && dir != ".") 
            {
                myStack.push_back(move(dir));
            }
        }
        string result;
        if (myStack.empty()) 
        {
            result = "/";
        }
        else 
        {
            for (string& dir: myStack) 
            {
                result += "/" + move(dir);
            }
        }
        return result;
    }
};