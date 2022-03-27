/*
0211 Design Add and Search Words Data Structure
Trie
*/

class WordDictionary {
    private Trie root; // root

    public WordDictionary() {
        root = new Trie(); // constructor
    }
    
    public void addWord(String word) {
        root.insert(word);
    }
    
    public boolean search(String word) {
        // Want to know if a word in the 'dictionary'
        return dfs(word, 0, root);
    }

    private boolean dfs(String word, int index, Trie node) {
        if (index == word.length()) {
            // Already traverse through the word,
            // Node need to be a terminated one 
            // To return true
            return node.isEnd();
        }
        char ch = word.charAt(index);
        if (Character.isLetter(ch)) {
            // Not a 'dot'
            int childIndex = ch - 'a';
            Trie child = node.getChildren()[childIndex];
            // Current node exist and recursive step also true.
            // Then true
            if (child != null && dfs(word, index + 1, child)) {
                return true;
            }
        } else {
            // Dot, just find the 26 alphabets
            // Any match, return true
            for (int i = 0; i < 26; i++) {
                Trie child = node.getChildren()[i];
                if (child != null && dfs(word, index + 1, child)) {
                    return true;
                }
            }
        }
        // Nothing matched, return False
        return false;
    }
}

class Trie {
    // Trie, a rooted tree
    // children, a pointer array
    // length would be 26, if we consider lowercase
    private Trie[] children;
    // isEnd, important, marks the termination of a string.
    private boolean isEnd;

    public Trie() {
        // Constructor, 
        // in our setting, trie has length 26
        children = new Trie[26];
        isEnd = false; // Empty
    }
    // Insert a word into current trie.
    public void insert(String word) {
        Trie node = this; // Start from current level
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            int index = ch - 'a'; // index in the array
            if (node.children[index] == null) {
                // null ptr, then init a new one
                node.children[index] = new Trie();
            }
            node = node.children[index];
        }
        // After processing, remember to set isEnd to true.
        node.isEnd = true;
    }

    public Trie[] getChildren() {
        // return all the consequtive characters
        return children;
    }

    public boolean isEnd() {
        // check if it reach the end
        return isEnd;
    }
}
/*
Credit:
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/solution/tian-jia-yu-sou-suo-dan-ci-shu-ju-jie-go-n4ud/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/
