#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
int mintime(int *b,float ti[]);

int main(){

float times[5];
int ba[5];

for(int i=1;i<=4;i++){
    times[i]=INFINITY;
    ba[i]=i;

}
times[1]=2;
times[2]=0.3;
times[3]=1.3;
times[4]=3.3;
printf("%d",mintime(ba,times));
// int *c = b;
// while(*c!=0){
//     printf("%d",*c);
//     c++;
// }
for(int j=1;j<=4;j++){
    printf("%d",ba[j]);
}

return 0;
}

int mintime(int *b,float ti[]){
float min = INFINITY;
int minat;

b++;
int *minadd = b;
while(*b!=0){

    if(ti[*b]<min){
            min=ti[*b];
            minat=*b;
            minadd =b;
            // printf("%d \n",minat);
    }
    // printf("%d \n",*b);
    b++;
}
b = minadd;
while(*b!=0){
    // printf("%d before change \n",*b);
    
    *b = *(minadd+1);
    // printf("%d after change \n",*b);
    b++;
    minadd++;

}
return minat; 
}