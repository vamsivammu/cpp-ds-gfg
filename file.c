#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){

char c[10000];

FILE *fp;
fp = fopen("file.txt","r");
if(fp==NULL){
    printf("not found");
}

fgets(c,1000,fp);
// int numcites= atoi(c);
// printf("%d",numcites+1);
fgets(c,1000,fp);
// numcites= atoi(c);
// printf("%d",numcites+1);
   fgets(c,1000,fp);
for(int i=0;i<2;i++){
    fgets(c,1000,fp);
char *token=strtok(c," ");
while(token!=NULL){
    printf("%s\n",token);
    token= strtok(NULL," ");
}
// printf("%s",c);

}

fclose(fp);
return 0;
}