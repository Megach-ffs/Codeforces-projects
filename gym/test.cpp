#include <bits/stdc++.h>
using namespace std;

vector<int> solvePermutation(int n) {
    vector<int> perm(n);
    vector<int> primes;
    
    // Precompute primes
    vector<bool> isPrime(2*n + 1, true);
    isPrime[0] = isPrime[1] = false;
    for (int i = 2; i <= 2*n; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
            for (int j = i * i; j <= 2*n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    // Construct permutation to maximize prime c_i
    int primeIndex = 0;
    for (int i = 0; i < n; i++) {
        // Ensure we have enough primes for future c_i calculations
        while (primeIndex < primes.size() && primes[primeIndex] <= 2*n/(i+1)) {
            primeIndex++;
        }
        
        // Place numbers to create prime c_i
        perm[i] = primes[primeIndex] * (i + 1) - (i > 0 ? accumulate(perm.begin(), perm.begin() + i, 0) : 0);
        primeIndex++;
    }
    
    return perm;
}

int main() {
    int n = 100000;
    
    // Precompute primes for verification
    vector<bool> primes(2*n + 1, true);
    primes[0] = primes[1] = false;
    for (int i = 2; i * i <= 2*n; i++) {
        if (primes[i]) {
            for (int j = i * i; j <= 2*n; j += i) {
                primes[j] = false;
            }
        }
    }
    
    vector<int> perm = solvePermutation(n);
    
    vector<int> ci(n);
    int sum = 0;
    int primeCi = 0;
    
    for (int i = 1; i <= n; i++) {
        sum += perm[i-1];
        ci[i-1] = sum / i;
        if (primes[ci[i-1]]) primeCi++;
    }
    
    cout << "Permutation size: " << n << endl;
    cout << "Number of prime c_i: " << primeCi << endl;
    cout << "Minimum required prime c_i: " << (n/3 - 1) << endl;
    
    return 0;
}
