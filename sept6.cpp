#include<iostream>
#include<algorithm>
using namespace std;
void show(int a[]){
    for(int i =0;i<10;i++){
    cout << a[i] << "";
}
}
int main(){

    int a[10] = {1,2,5,6,9,0,3,4,8,7};
    show(a);
    sort(a,a+10);
    cout << endl;
    show(a);
    return 0;
}