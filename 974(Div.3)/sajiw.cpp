

// vector <int> merge(vector <int> a, vector <int> b){
//     int n=a.size();
//     int m=b.size();
//     int i=0, j=0, c=0;
//     vector <int> res(m+n);
//     while (j<m or i<n){
//         if (j>m or (i<n and a[i]<b[j])){
//             res[c]=a[i];
//             c++;i++;
//         } else {
//             res[c]=b[j];
//             c++;i++;
//         }
//     }
//     return res;
// }

// int main(){
//     int n;
//     cin>>n;
//     vector <int> a(n);
//     for (int i=0; i<n; i++) cin>>a[i];
//     vector <int> b(2*n);
//     b=merge(a,a);
//     for (int i=0; i<2*n; i++) cout<<b[i]<<" ";
// }

#include <iostream>
using namespace std;

int main()
{
    for (size_t i = 0; i < 100; i++)
    {
        cout<<"Hello World"<<endl;
        /* code */
    }
    

    return 0;
}