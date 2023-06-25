#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

char alpha [256];

template <typename T>
void print_vector(vector<T> &letters){
    for (const auto &item : letters) {
        cout << item << "; ";
    }
    cout << endl;
}

int check(vector<string> &word_list, vector<char> &letters, vector<int> &numbers){
    int m = letters.size();
    int i;
    int ans = 0;
    for (i=0; i<m; i++){
        alpha[letters[i]] = numbers[i];
    }
    for (i=0; i<word_list.size(); i++){
        int now = 0;
        for (char x :word_list[i]){
            now = now * 10 + alpha[x];
        }
        ans += now;
    }
    return ans;
}

int main(){
    int N, i;
    cin >> N;
    int ans = 0;
    int now = 0;
    vector<string> word_list(N);
    vector<char> letters;
    for(i=0; i<N; i++){
        cin >> word_list[i];
        for (char x : word_list[i]){
            letters.push_back(x);
        }
    }
    sort(letters.begin(), letters.end());
    letters.erase(unique(letters.begin(), letters.end()), letters.end());
    vector<int> numbers;
    for (int j=10-letters.size(); j<10; j++){
        numbers.push_back(j);
    }
    do{
        now = check(word_list, letters, numbers);
        if (ans < now){
            ans = now;
        }
    }while(next_permutation(letters.begin(), letters.end()));
    cout << ans <<endl;
}