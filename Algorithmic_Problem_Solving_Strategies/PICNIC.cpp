#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<vector>

using namespace std;

// 0,1 2,3 || 0,2 1,3 || 0,3 2,1
// 학생 쌍이 1개인 경우

int picnic(vector<int>& number_students, bool save_vec[][10], bool taken[10]){
    int i, j, ret=0;
    int firstFree = -1;
    for(i =0; i<number_students[0]; i++){
        if(!taken[i]){
            firstFree = i;
            break;
        }
    }
    if(firstFree == -1){
        return 1;
    }
    for(j=firstFree+1; j < number_students[0]; j++){
        if(!taken[j] && save_vec[firstFree][j]==true){
            taken[firstFree] = taken[j] = true;
            ret += picnic(number_students, save_vec, taken);
            taken[firstFree] = taken[j] = false;
        }
    }
    return ret;
}

int main(){
    // test case number
    int test_case;
    int first, second, temp;
    int i, j, answer;
    int count = 0;
    vector<int> answers;
    cin >> test_case;
    for (i=0; i<test_case; i++){
        vector<int> number_student;
        vector<int> pare_freinds;
        bool areFreinds[10][10]= {false,};
        bool taken[10] = {false,};
        for (j=0; j<2;j++){
            cin >> temp;
            number_student.push_back(temp);
        }
        for(j=0; j<(number_student[1]); j++){
            cin >> first >> second;
            count++;
            if(count == 1){
                count = 0;
                areFreinds[first][second] = true;
                areFreinds[second][first] = true;
            }
        }
        answer = picnic(number_student, areFreinds, taken);
        answers.push_back(answer);
    }
    for(auto& x : answers){
        cout << x << endl;
    }
}