#include<bits/stdc++.h>

using namespace std;

int main(){

	int t;
	cin >> t;
	for (int i=0; i<t; i++){
		long long x, y, a, count;
		count = 0;
		cin>>x>>y>>a;
		count = a % (x + y);
		if ( count - x < 0) { cout << "NO"<<endl;}
		else {cout<<"YES"<<endl;}	
	}
	return 0;

}
