/** 
0706 Design Hash Map
A quick recap of Java
*/
class MyHashMap {
    private class hashPair {
        // Define a class to store key-value pair.
        private int key;
        private int value;
        public hashPair(int key, int value) {
            // init
            this.key = key;
            this.value = value;
        }
        // Define some public methods,
        // Avoid directly using .key, .value.
        public int getKey() {
            return key;
        }
        public int getValue() {
            return value;
        }
        public void setValue(int value) {
            this.value = value;
        }
    }
    // Similar setting as LeetCode 705
    private static final int BASE = 769;
    private LinkedList[] data;
    public MyHashMap() {
        data = new LinkedList[BASE];
        for (int i=0; i < BASE; i++) {
            // the element of data[i] is 
            // hashPair LinkedList 
            data[i] = new LinkedList<hashPair>(); 
        }
    }
    
    private static int hash(int key) {
        // helper method to compute hash value
        return key % BASE;
    }
    
    public void put(int key, int value) {
        int hashValue = hash(key);
        // Use iterator like a cursor.
        Iterator<hashPair> iterator = data[hashValue].iterator();
        while (iterator.hasNext()) {
            hashPair pair = iterator.next();
            if (pair.getKey() == key) {
                pair.setValue(value);
                return;
            }
        }
        // offerLast, insert to the end.
        data[hashValue].offerLast(new hashPair(key, value));
    }
    
    public int get(int key) {
        int hashValue = hash(key);
        Iterator<hashPair> iterator = data[hashValue].iterator();
        while (iterator.hasNext()) {
            hashPair pair = iterator.next();
            if (pair.getKey() == key) {
                return pair.getValue();
            }
        }
        // Not found
        return -1;     
    }
    
    public void remove(int key) {
        int hashValue = hash(key);
        Iterator<hashPair> iterator = data[hashValue].iterator();
        while (iterator.hasNext()) {
            hashPair pair = iterator.next();
            if (pair.getKey() == key) {
                // remove the element using given method.
                data[hashValue].remove(pair);
                return;
            }
        }       
    }
}
/**
Credit: 
@ Leetcode-Solution,
Link: https://leetcode-cn.com/problems/design-hashmap/solution/she-ji-ha-xi-ying-she-by-leetcode-soluti-klu9/
 */