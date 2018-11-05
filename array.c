#include<stdio.h>
void push(int *b,int ele);
int isempty(int *b);
int pop(int *b);
int topstack =-1;
int maxsize= __INT_MAX__;
int main(){



    int a[10];

    push(a,2);
    push(a,4);
    push(a,1);
    printf("%d \n",a[0]);

    printf("%d \n",a[1]);
    printf("%d \n",a[2]);
    printf("%d \n",pop(a));   
     push(a,5);
    printf("%d \n",a[0]);

    printf("%d \n",a[1]);
    printf("%d \n",a[2]);
   printf("%d",topstack);
   for(int j=0;j<=topstack;j++){
       printf("%d \n",a[j]);
   }
    return 0;

}

void push(int *b,int ele){

topstack =topstack+1;
b = b + topstack;
*b =ele;
}
int pop(int *b){

    b = b+topstack;
    int data = *b;
    topstack= topstack-1;
    return data;

}
int isempty(int *b){
if(topstack == -1){
    return 0;
}
return 1;
        
}