/**
0460 LFU Cache
Hash Map + Balanced Binary Tree
Credit: Leetcode-CN-Solution
*/
// We first need to define a cache unit.
struct Node
{
    // Count: How many times the node is used
    int count;
    // Timestamp: most recent usage timestamp
    int timestamp;
    int key, value;
    
    Node(int _count, int _timestamp, int _key, int _value) : count(_count), timestamp(_timestamp), key(_key), value(_value) {} 
        
    // Comparator
    bool operator< (const Node &rhs) const
    {
        return count == rhs.count ? timestamp < rhs.timestamp : count < rhs.count;
    }
};

class LFUCache 
{
    // Capacity & timestamp
    int capacity, time;
    unordered_map<int, Node> key_table;
    // Behind the scene, C++ set use RB Tree.
    set<Node> S;
    
public:
    LFUCache(int _capacity) 
    {
        capacity = _capacity;
        time = 0;
        key_table.clear();
        S.clear();
    }
    
    int get(int key) 
    {
        if (capacity == 0) return -1;
        auto item = key_table.find(key);
        // Not found
        if (item == key_table.end()) return -1;
        // Get previous cache
        Node cache = item -> second;
        S.erase(cache);
        // Update information in the cache unit
        cache.timestamp = ++time;
        cache.count += 1;
        // Place back into the set and update hashtable's info
        S.insert(cache);
        item -> second = cache;
        return cache.value;
    }
    
    void put(int key, int value) 
    {
        if (capacity == 0) return;
        auto item = key_table.find(key);
        if (item == key_table.end()) 
        {
            // Reach capacity, have to remove LFU
            if (key_table.size() == capacity) 
            {
                key_table.erase(S.begin() -> key);
                S.erase(S.begin());
            }
            Node new_cache = Node(1, ++time, key, value);
            key_table.insert(make_pair(key, new_cache));
            S.insert(new_cache);
        }
        else 
        {
            // Do some updates
            Node cache = item -> second;
            S.erase(cache);
            // Update information in the cache unit
            cache.timestamp = ++time;
            cache.value = value;
            cache.count += 1;
            // Place back into the set and update hashtable's info
            S.insert(cache);
            item -> second = cache;          
        }
    }
};