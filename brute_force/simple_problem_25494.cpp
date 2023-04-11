#include<iostream>
#include<vector>

using namespace std;

int SimpleNumber(int* three_num){
    int i, j, k, count = 0;
    for(i = 1; i <= three_num[0]; i++){
        for(j=1; j<= three_num[1]; j++){
            for(k=1; k<= three_num[2]; k++){
                if((i%j)==(j%k) && (j%k)==(k%i) && (i%j)==(k%i)){
                    count+=1;
                }
            }
        }
    }
    return count;
}

int main(){
    int input_num, i, j;
    vector<int> result;
    int three_num[3];
    cin >> input_num;
    for(i=0; i<input_num; i++){
        
        int result;
        for(j=0; j<3; j++){
            cin >> three_num[j];
        }
        cout << SimpleNumber(three_num) <<endl;
    }
}