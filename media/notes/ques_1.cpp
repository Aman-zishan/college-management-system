#include <bits/stdc++.h>

using namespace std;
class batsman{
    char name[100];
    int innings, notout, runs;
    float batavg;
    void calcbatavg(){
        batavg = (float)runs/(innings-notout);
    }
    public:
    void getdata();
    void displaydata();
};

void batsman::getdata(){
    cout<<"Enter the name of the batsman: ";
    cin.getline(name,100);
    cout<<"Enter the number of innings played by the batsman: ";
    cin>>innings;
    cout<<"Enter number of notouts: ";
    cin>>notout;
    cout<<"Enter runs scored: ";
    cin>>runs;
    calcbatavg();
    displaydata();
}

void batsman::displaydata(){
    cout<<"Name of batsman: "<<name<<endl;
    cout<<"Innings: "<<innings<<endl;
    cout<<"Notout: "<<notout<<endl;
    cout<<"Runs: "<<runs<<endl;
    cout<<"Bating average: "<<batavg<<endl;
}
int main() {
    cout<<"**********************************\n";
    cout<<"Name : Bennett B Madavana\nRoll no:34\nBatch : IT- A\n";
    cout<<"**********************************\n\n";
   batsman b;
   b.getdata();
}
