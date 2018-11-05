#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
void printpath(int b[],int dest);
void push(int *b,int ele);
int pop(int *b);
int isempty(int *b);
int contains(int *b,int sr);
float toRadians(const float degree);
void minpush(int *b,int ele);
float distance(float lat1, float long1,  
                     float lat2, float long2);
int mindist(int *b,float times[]);
void pathpush(int *b,int ele);
struct node{
    int nodenum;
    float lat;
    float longitude;

};
int pathstack =-1;
int path[10000000];
struct element{

    struct node fn;
    struct node bn;
    float t;

};
int topstack = -1;
int topminstack= -1;
int main(){
float speed = 100;

// struct node n1,n2,n3,n4,n5;
// n1.nodenum=1;
// n2.nodenum=2;
// n3.nodenum=3;
// n4.nodenum=4;
// n5.nodenum=5;
// struct element e1,e2,e3,e4,e5;
// e1.bn = n2;
// e1.fn= n1;
// e2.bn=n2;
// e2.fn=n4;
// e3.fn=n3;
// e3.bn=n4;
// e4.bn=n1;
// e4.fn=n4;
// e5.fn=n3;
// e5.bn=n1;
// e1.t=1;
// e2.t=2;
// e3.t=5;
// e4.t=0.5;
// e5.t=6;
// arrayelement[1]=e1;
// arrayelement[2]=e2;
// arrayelement[3]=e3;
// arrayelement[4]=e4;
// arrayelement[5]=e5;

char c[10000];

FILE *fp;
fp = fopen("file.txt","r");
if(fp==NULL){
    printf("not found");
}

fgets(c,1000,fp);
int numcites= atoi(c);

fgets(c,1000,fp);
int numroads= atoi(c);
float times[numroads+1];
int parents[numcites+1];
for(int j=1;j<=numcites;j++){
    times[j]=INFINITY;

}
struct node arraynode[numcites+1];
struct element arrayelement[numroads+1];

for(int p=1;p<=numcites;p++){
    parents[p]=0;
}

fgets(c,1000,fp);
fgets(c,1000,fp);

for(int cities =1;cities<=numcites;cities++){
    struct node city;
    
    fgets(c,1000,fp);
    char *tokens= strtok(c," ");
    int j=0;
    double token[3];
    while(tokens!=NULL){
        token[j]=(double)(atof(tokens));
        // printf("%f \n",token[j]);

        j=j+1;
    tokens= strtok(NULL," ");
}
city.nodenum=token[0];
city.lat=token[1];
city.longitude=token[2];
// printf("%d",city.nodenum);
arraynode[cities]=city;
}
fgets(c,1000,fp);
fgets(c,1000,fp);
for(int roads=1;roads<=numroads;roads++){
struct element road;
fgets(c,1000,fp);
char *roadtoken=strtok(c," ");
 int j=0;
  int token[3];
    while(roadtoken!=NULL){
        token[j]=(int)(atof(roadtoken));
        // printf("%d \n",token[j]);

        j=j+1;
    roadtoken= strtok(NULL," ");
}
// printf("completed");
// printf("%d",token[0]);
road.bn=arraynode[token[0]];
road.fn=arraynode[token[1]];
// printf("%f",road.bn.lat);
road.t = distance(road.bn.lat,road.bn.longitude,road.fn.lat,road.fn.longitude)/speed;
// printf("%f \n",road.t);
arrayelement[roads]=road;
// printf("%d",roads);
}

int stack[numcites+1];
int minstack[numcites+1];
fgets(c,1000,fp);
fgets(c,1000,fp);

int nodesrc = atoi(c);
fgets(c,1000,fp);
fgets(c,1000,fp);
int destination=atoi(c);

times[nodesrc]=0;
// printf("%d %d",nodesrc,destination);
for(int s =0;s<=numcites;s++){
    stack[s]=0;
}
for(int r =0;r<=numcites;r++){
    minstack[r]=0;
}
path[numcites+1];
for(int v=0;v<=numcites;v++){
    path[v]=0;
}
push(stack,nodesrc);

// printf("%d",stack[0]);
while(isempty(stack)==1){
    // printf("Inside djkistra");
        int src = mindist(stack,times);
        // printf("%d minimum \n",src);
        if(contains(minstack,src)==0){
                    minpush(minstack,src);
        for(int i = 1;i<=numroads;i++){
            // printf("%d",contains(minstack,src));

                    if(arrayelement[i].bn.nodenum==src && contains(minstack,arrayelement[i].fn.nodenum)==0){
                
                            // printf("%d \n",arrayelement[i].fn.nodenum);
                if(arrayelement[i].t+times[src]<=times[arrayelement[i].fn.nodenum]){
                        // printf("%f \n",arrayelement[i].t+times[src]);
                        
                        times[arrayelement[i].fn.nodenum]=arrayelement[i].t+times[src];
                        parents[arrayelement[i].fn.nodenum]=src;
                        // printf("%d \n",src);
                }
                                    if(contains(stack,arrayelement[i].fn.nodenum)==0){
                            push(stack,arrayelement[i].fn.nodenum);
                }
                // printf("%f",times[arrayelement[i].fn.nodenum]);
                
                
            }
            if(arrayelement[i].fn.nodenum==src && contains(minstack,arrayelement[i].bn.nodenum)==0){
                // printf("%d",src);
                // printf("%d \n",arrayelement[i].bn.nodenum);
                if(arrayelement[i].t+times[src]<=times[arrayelement[i].bn.nodenum]){
                        // printf("%f \n",arrayelement[i].t+times[src]);
                        
                        times[arrayelement[i].bn.nodenum]=arrayelement[i].t+times[src];
                        parents[arrayelement[i].bn.nodenum]=src;
                        // printf("%d \n",src);
                }

                if(contains(stack,arrayelement[i].bn.nodenum)==0){
                            
                            push(stack,arrayelement[i].bn.nodenum);
                    // printf("pushed");
                }
                
                // printf("%f",times[arrayelement[i].fn.nodenum]);
               
                
            }
            
            
        }

        }
        

}
// for(int k=1;k<=numcites;k++){
//     printf("%d",parents[k]);
// }
float totaltime=0;
float ttime =0;
int days=0;
printpath(parents,destination);
int *pathpointer = &path[0];
int *pp = pathpointer;
while(*pathpointer!=0){
    
    for(int eleme=1;eleme<=numroads;eleme++){
     if((arrayelement[eleme].bn.nodenum==*(pp+1) && arrayelement[eleme].fn.nodenum==*pathpointer) || (arrayelement[eleme].fn.nodenum==*(pp+1) && arrayelement[eleme].bn.nodenum==*pathpointer)){

if(ttime+arrayelement[eleme].t>10){
    // totaltime = ttime+arrayelement[eleme].t+24;
    days = days+1;
    ttime =arrayelement[eleme].t;
    
}else{
    ttime = ttime+arrayelement[eleme].t;
}
     }   
    }
    pathpointer++;
    pp++;
}
printf("%d days %f hours",days,ttime);
return 0;


}
void printpath(int b[],int dest){
if(b[dest]==0){
printf("%d > \n",dest);
pathpush(path,dest);
return;
}
printpath(b,b[dest]);
printf("%d >\n",dest);
pathpush(path,dest);

}
void pathpush(int *b,int ele){
    pathstack = pathstack+1;
    b = b+pathstack;
    *b = ele;

}
void push(int *b,int ele){

topstack =topstack+1;
b = b + topstack;
*b =ele;
// b = b-topstack;
// while(*b!=0){
//     printf("%d",*b);
//     b++;
// }
}
int pop(int *b){

    b = b+topstack;
    int data = *b;
    topstack= topstack-1;
    return data;

}
int isempty(int *b){
    // printf("%d topstack\n",topstack);
if(topstack == -1){
    return 0;
}
return 1;
        
}
void minpush(int *b,int ele){

topminstack =topminstack+1;
b = b + topminstack;
*b =ele;
}
int mindist(int *b,float times[]){
// printf("%d \n",topstack);
// printf("%d \n",*(b+2));
float min = INFINITY;
int minat;
int *minadd = b;

// printf("%d starting \n",*b);
while(*b!=0){
    // printf("%d in while loop \n",*b);
    if(times[*b]<=min){
        min=times[*b];
        minat = *b;
        minadd=b;
    }
    b++;
}

b--;
// printf("%d ending \n",*b);
b=minadd;
while(*b!=0){
    // printf("%d before removal \n",*b);
    *b =*(minadd+1);
    // printf("%d after removal \n",*b);
    
    b++;
    minadd++;
}
topstack = topstack-1;
// printf("%d \n",topstack);
return minat;    
}
int contains(int *b,int sr){
    
    while(*b!=0){
        if(*b==sr){
            return 1;
        }
        b++;
    }
    return 0;
}
int containsstack(int *b,int sr){
        
    while(*b!=0){
        if(*b==sr){
            return 1;
        }
        b++;
    }
    return 0;
}
int minpop(int *b){

    b = b+topminstack;
    int data = *b;
    topminstack= topminstack-1;
    return data;

}
int isemptymin(int *b){
if(topminstack == -1){
    return 0;
}
return 1;
        
}
float toRadians(const float degree) 
{ 
    // cmath library in C++  
    // defines the constant 
    // M_PI as the value of 
    // pi accurate to 1e-30 
    float one_deg = 3.1416 / 180; 
    return (one_deg * degree); 
} 
  
float distance(float lat1, float long1,  
                     float lat2, float long2) 
{ 
    // Convert the latitudes  
    // and longitudes 
    // from degree to radians. 
    lat1 = toRadians(lat1); 
    long1 = toRadians(long1); 
    lat2 = toRadians(lat2); 
    long2 = toRadians(long2); 
    //   printf("%f",lat2);
    // Haversine Formula 
    float dlong = long2 - long1; 
    float dlat = lat2 - lat1; 
  
    float ans = pow(sin(dlat / 2), 2) +  
                          cos(lat1) * cos(lat2) *  
                          pow(sin(dlong / 2), 2); 
  
    ans = 2 * asin(sqrt(ans)); 
  
    // Radius of Earth in  
    // Kilometers, R = 6371 
    // Use R = 3956 for miles 
    float R = 6371; 
      
    // Calculate the result 
    ans = ans * R; 
  
    return ans; 
}