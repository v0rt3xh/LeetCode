/**
 * 0232 Implementing Queue Using Stack
 * Using two stacks
 * 
 */
class MyQueue {
private: 
    stack<int> inStack, outStack;
    // Helper method, move elements in inStack to outStack
    void in2out() {
        while(!inStack.empty()) {
            outStack.push(inStack.top());
            inStack.pop();
        }
    }
public:
    MyQueue() {
        
    }
    
    void push(int x) {
        // regular push
        inStack.push(x);
    }
    
    int pop() {
        // Important design, we move elements from inStack to outStack
        // When outStack is empty
        if (outStack.empty()) {
            in2out();
        }
        int x = outStack.top();
        outStack.pop();
        return x;
    }
    
    int peek() {
        // Similar to pop
        if (outStack.empty()) {
            in2out();
        }
        return outStack.top();
    }
    
    bool empty() {
        // Need both stacks to be empty
        return inStack.empty() && outStack.empty();
    }
};