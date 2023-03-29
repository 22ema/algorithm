#include<iostream>
#include<string>
using namespace std;

class Something{
public:
    string m_value = "default";
    const string& getValue() const {return m_value;}
    string& getValue(){return m_value;}
};

void print(Something st){
    cout << st.m_value << endl;
}

int main (){
    Something something;
    something.getValue();

    const Something something2;
    something2.getValue();
}