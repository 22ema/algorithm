#include<stdio.h>
#include<iostream>
#include<vector>

using namespace std;

const int blocks[4][3][2]=   {
                    {{0, 0}, {0, 1}, {-1, 1}},
                    {{0, 0}, {0, 1}, {1, 1}},
                    {{0, 0}, {0, 1}, {1, 0}},
                    {{0, 0}, {1, 0}, {1, 1}}
                    };

int set(vector<vector<int>> &board, int y, int x, int types, int delta){
    int i, j;
    bool ok = true;
    for(i=0; i<3; i++){
        int nx = x + blocks[types][i][0];
        int ny = y + blocks[types][i][1];
        if (nx < 0 || ny < 0 || ny >= board.size() || nx >= board[0].size()) {
            ok = false;
        }
        else if((board[ny][nx] += delta) > 1){
            ok = false;
        } 
    }
    return ok;
}

int boardCover(vector<vector<int>>& b_game_map){
    int i, j, y=-1, x=-1, ret = 0;
    for (i=0; i<b_game_map.size(); i++){
        for (j=0; j< b_game_map[0].size(); j++){
            if (b_game_map[i][j] == 0){
                y = i;
                x = j;
                break;
            }
        }
        if(y!= -1) break;
    }
    if(y == -1) return 1;
    for (i=0; i<4; i++){
        if(set(b_game_map, y, x, i, 1)){
            ret+= boardCover(b_game_map);
        }
        set(b_game_map, y, x, i, -1);
    }
    return ret;
}

int main(){
    int test_case = 0;
    int answer = 0;
    vector<int> answers;
    int i, j, k, temp;
    

    cin >> test_case;

    for (i=0; i<test_case; i++){
        vector<int> game_map_shape;
        int num_white_blocks = 0;
        for(j=0; j<2; j++){
            cin >> temp;
            game_map_shape.push_back(temp);
        }
        vector<vector<char>>  game_map(game_map_shape[0],vector <char>(game_map_shape[1],0));
        vector<vector<int>> b_game_map(game_map_shape[0],vector <int>(game_map_shape[1],0));

        for (j=0; j<game_map_shape[0]; j++){
            for (k=0; k<game_map_shape[1]; k++){
                cin >> game_map[j][k];
                if (game_map[j][k] == '#'){
                    b_game_map[j][k] = 1;
                }
                else{
                    num_white_blocks++;
                }
            }
        }
        if(num_white_blocks%3!=0){
            answers.push_back(0);
        }
        else{
            answer = boardCover(b_game_map);
            answers.push_back(answer);
        }
        //함수를 여기 입력하면 될듯함
    }
    for(auto & x : answers){
        cout << x << endl;
    }
}