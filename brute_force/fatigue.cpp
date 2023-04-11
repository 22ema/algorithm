#include <string>
#include <vector>
#include <iostream>

using namespace std;

int maximum = -1;

int loop_dungeons(int k, vector<vector<int>>dungeons,  vector<bool> visited, int answer){
    int dungeons_size = dungeons.size();
    int i, finished = 1;
    for(i=0; i<dungeons_size; i++){
        if(k >= dungeons[i][0] && visited[i]==false){
            
            finished = 0;
        }
    }
    if(finished==1){
        if (maximum < answer){
            cout << k << endl;
            maximum = answer;
        }
        return answer;
    }
    for(i=0; i<dungeons_size; i++){
        if(visited[i] == true || k < dungeons[i][0]) continue;
        visited[i] = true;
        k -= dungeons[i][1];
        answer += 1;
        loop_dungeons(k, dungeons, visited, answer);
        answer -= 1;
        k += dungeons[i][1];
        visited[i] = false;
    }
    return answer;
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = 0;
    int dungeons_size = dungeons.size();
    vector<bool> visited (dungeons_size, false);
    answer = loop_dungeons(k, dungeons, visited, answer);
    return maximum;
}

int main(){
    vector<vector<int>> dungeons = {{80, 20},{50, 40}, {30, 10}};
    int result = solution(80, dungeons);
    return 0;
}