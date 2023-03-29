#include <string>
#include <vector>
#include <iostream>

#define INF 1000000
using namespace std;

int bigNum(int x, int y){
    if (x > y) return x;
    else return y;
}

int minNum(int x, int y){
    if (x < y) return x;
    else return y;
}

void swap(int& x, int& y){
    int temp=0;
    temp = x;
    x = y;
    y = temp;
}


int makeWallet(vector<vector<int>> sizes){
    int i, j;
    int lmax = 0;
    int rmax = 0;
    int size = sizes.size();
    for(i=0; i<size; i++){
        if(sizes[i][0] > sizes[i][1]) continue;
        else swap(sizes[i][0], sizes[i][1]);
    }
    for(i=0; i<size; i++){
        if(lmax < sizes[i][0]){
            lmax = sizes[i][0];
        }
        if(rmax < sizes[i][1]){
            rmax = sizes[i][1];
        }
    }
    return lmax * rmax;
}

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    answer = makeWallet(sizes);
    return answer;
}