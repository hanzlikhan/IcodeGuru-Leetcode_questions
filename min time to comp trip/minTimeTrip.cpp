#include <iostream>
using namespace std;
int main(){
    int arr[1,2,3,4,5];
    int bus1 = 0;
    int bus2 = 0;
    int bus3 = 0;
    for(int i=1;i<5;i++){
        bus1++;
        if(arr[i]%2==0){
            bus2+=2;
        }
        if(arr[i]%3==0){
             bus3+=3;
        }
    }
    int totaltime = bus1+bus2+bus3;
    if(totaltime==5)
}