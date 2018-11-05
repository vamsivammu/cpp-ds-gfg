#include<iostream>
#include<algorithm>
#include<iterator>
#include<vector>
using namespace std;
int main(){

        vector<int> vect;
        for(int i =1;i<10;i++){
            vect.push_back(i);
        }
for(vector<int> ::iterator it=vect.begin();it!=vect.end();++it){
    cout << *it;
}

    return 0;
}