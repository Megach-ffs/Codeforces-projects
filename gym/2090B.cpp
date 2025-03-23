#include<bits/stdc++.h>

using namespace std;

bool checker(const vector<vector<int>>& matrix, int x, int y);

int main(){


	int t;
	cin>>t;
	for (int i =0; i<t; i++){

		int x,y;
		vector<vector<int>> matrix;
		cin>>x>>y;
		cin.ignore();

		for (int j =0; j<x; j++){
			string line;
			getline(cin, line);

			vector<int> row;
			for (char ch : line){
				row.push_back(ch - '0');
			}
		matrix.push_back(row);
		}

		cout << (checker(matrix, x, y) ? "YES" : "NO") << endl;	


	}	

	return 0;
}

bool checker(const vector<vector<int>>& matrix, int x, int y){


	for (int i =0; i<x; i++){

		for (int j=0; j<y; j++){

			if (matrix[i][j] == 1){
			
				bool yes = true;
				for (int k = 0; k<i; k++){
					if (matrix[k][j] == 0){
						yes = false;
						break;
					}
				}
				if (yes) {continue;}	
				yes = true;
				for (int k = 0; k<j; k++){
					if (matrix[i][k] == 0){
						yes = false;
						break;
					}
				}
				if (!yes){return false;}	
			}	
		}
	}


	return true;
}
