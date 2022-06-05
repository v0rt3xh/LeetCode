/**
0204 Count Primes
Eratosthenes' method
*/
class Solution {
public:
    int countPrimes(int n) 
    {
        vector<int> isPrime(n, 1);
        int result = 0;
        for (int i = 2; i < n; i++) 
        {
            if (isPrime[i]) // is prime: add up result
            {
                result += 1;
                // Also rule out composite numbers!
                if ((long long) i * i < n) // Could out of scope.
                {
                    for (int j = i * i; j < n; j += i) 
                    {
                        isPrime[j] = 0;
                    }
                }
            }
        }
        return result;
    }
};