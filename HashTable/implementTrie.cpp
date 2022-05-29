class Trie {
private:
    // array of pointers and terminating indicator
    vector<Trie*> children;
    bool isEnd;
    // Private helper method, 
    Trie* searchPrefix(string prefix) {
        Trie* node = this;
        // Traverse through all the characters
        for (char character: prefix) {
            character -= 'a';
            // If meet nullptr, just return nullptr, 'Not found'
            if (node->children[character] == nullptr) {
                return nullptr;
            }
            // move the cursor
            node = node->children[character];
        }
        return node;
    }
    
public:
    // constructor
    Trie() : children(26), isEnd(false) {}
    
    void insert(string word) {
        Trie* node = this;
        for (char character: word) {
            character -= 'a';
            if (node->children[character] == nullptr) {
                node->children[character] = new Trie();
            }
            node = node->children[character];
        }
        // At the 'End', set the indicator to true.
        node->isEnd = true;
    }
    
    bool search(string word) {
        // Determine if a word is in the trie
        // 1: search result is not null
        // 2: isEnd is True!
        Trie* searchResult = this->searchPrefix(word);
        return searchResult != nullptr && searchResult->isEnd;
    }
    
    bool startsWith(string prefix) {
        // Starting with 'abcd', 
        // Search result is not null
        return this->searchPrefix(prefix) != nullptr;
    }
};
