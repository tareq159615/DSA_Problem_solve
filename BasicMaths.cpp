#include<bits/stdc++.h>
using namespace std; 
// void ArmstrongNumber(int n){
//     vector<int> ls; 
//     for (int i = 0; i*i <= n; i++){
//         if (n % i == 0){
//            ls.push_back(i); 
//            if((n/i) != i){
//             ls.push_back(n/i); 
//            }
//         }
//     }
//     sort(ls.begin(), ls.end()); 
//     for (auto it : ls) cout << it << " "; 
// }


void primeNumber(int n){
    int count = 0; 
    for (int i = 1; i <= n; i++){
       if (n%i == 0){
        count++; 
       }
    }
    if (count == 2){
        cout << "it's prime number"; 
    }else{
        cout << "it's a not prime number"; 
    }

}


int main (){
    int n; 
    cin >> n; 
    primeNumber(n); 
}