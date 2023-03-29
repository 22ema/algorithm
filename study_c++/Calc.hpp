#pragma once

#include <iostream>
using namespace std;

class Calc{
    private:
        int m_value;
    public:
        Calc(int init_value);
        ~Calc();
        void add(int value) {m_value += value;}
        void sub(int value) {m_value -= value;}
        void mult(int value) {m_value *= value;}

        void print(){
            cout << m_value << endl;
        }
};