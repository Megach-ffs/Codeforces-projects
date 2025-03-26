
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    const int MAXP = 100000;
    vector<bool> isPrime(MAXP+1,true);
    isPrime[0]=isPrime[1]=false;
    for(int i=2;i*i<=MAXP;i++){
        if(isPrime[i]){
            for(int j=i*i;j<=MAXP;j+=i)
                isPrime[j]=false;
        }
    }
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        int k = n/3;
        if(k == 0) k = 1;
        int A = max(2, k);
        int B = (2*n + 2) / 3;
        int p = -1;
        for (int x = A; x <= B; x++){
            if(isPrime[x]){
                p = x;
                break;
            }
        }
        vector<int> perm;
        vector<bool> used(n+1, false);
        int blockLength = 2 * k - 1;
        vector<int> block;
        for (int i = 0; i < k; i++){
            if(i == 0) block.push_back(p);
            else{
                block.push_back(p - i);
                block.push_back(p + i);
            }
        }
        for (auto x : block){
            if(x >= 1 && x <= n && !used[x]){
                perm.push_back(x);
                used[x] = true;
            }
        }
        for (int x = 1; x <= n; x++){
            if(!used[x]){
                perm.push_back(x);
                used[x] = true;
            }
        }
        for (int i = 0; i < n; i++){
            cout << perm[i] << (i == n-1 ? "\n" : " ");
        }
    }
    return 0;
}

