'''
0029 Divide two integers
Given two integers dividend and divisor,
divide two integers without using multiplication, division, and mod operator.
java though
'''
public int divide(int dividend, int divisor) { // 被除数 除数
        if(divisor == -1 && dividend == Integer.MIN_VALUE) return Integer.MAX_VALUE; // 溢出
        int sign = 1;
        if((dividend > 0 && divisor < 0)||(dividend < 0 && divisor > 0))
            sign = -1;
        int a = dividend>0 ? -dividend : dividend;
        int b = divisor>0 ? -divisor : divisor;
        // 都改为负号是因为int 的范围是[-2^31, 2^31-1]，如果a是-2^31，转为正数时将会溢出
        if(a > b) return 0;
        int ans = div(a,b);
        return sign == -1 ? -ans : ans;
    }
    int div(int a, int b)
    {
        // Notice that we are considering negative case!
        if(a > b) return 0;
        int count = 1;
        // 60 / 8 = (60 - 32) / 8 + 4 = (60 - 32 - 16) / 8 + 2 + 4
        int tb = b; // The divisor 
        while(tb+tb >= a && tb+tb < 0){ // 溢出之后不再小于0: tb + tb < 0
            tb += tb;
            count += count;
        }
        return count+div(a-tb,b);
    }




