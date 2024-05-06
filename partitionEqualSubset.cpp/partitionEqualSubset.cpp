#include <iostream>
#include<vector>
using namespace std;
bool solve(int ind,vector<int>arr,int n,int target){
    // base case 
    if (ind>n){
        return 0;
    }
    if(target < 0){
        return 0;
    }
    if(target == 1){
        return 1;
    }
    bool inc = solve(ind+1,arr,n,target-arr[ind]);
    bool exl = solve(ind+1,arr,n,target-0);
    return inc or exl;
}
int main(){
    vector<int> arr  = {1,5,11,5};
    int sum = 0;
    int n = arr.size();
    for(int i = 0;i<n;i++){
        sum += arr[i];
    }
    if(sum & 1)
    cout<<0;
    int target = sum/2;
    result = solve(0,arr,n,target);

}
