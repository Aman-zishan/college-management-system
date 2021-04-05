#include<iostream>
using namespace std;

class vector{
    int vect[20], n;
    public:

    void createVect(){
        cout<<"Enter the number of coordinates: ";
        cin>>n;
        cout<<"Enter the coordinates: ";
        for(int i=0; i<n; i++){
            cin>>vect[i];
        }
        displayVect();
    }

    void modifyVect(){
        int loc, num;
        cout<<"Enter location of coordinate to update: ";
        cin>>loc;
        cout<<"Enter new value: ";
        cin>>num;
        vect[loc-1] = num;
        displayVect();
    }

    void multiplyByScalar(){
        int scalar;
        cout<<"Enter scalar: ";
        cin>>scalar;
        for(int i= 0; i<n; i++){
            vect[i]*=scalar;
        }
        displayVect();
    }

    void displayVect(){
        cout<<"The vector is: ("<<vect[0];
        for(int i=1; i<n; i++){
            cout<<", "<<vect[i];
        }
        cout<<")"<<endl;
    }
};

int main(){
    cout<<"**********************************\n";
    cout<<"Author Name : Aparna Sathyanathan\nRoll no: 23\nBatch : IT- A\n";
    cout<<"**********************************\n";
    int opt;
    char ch;
    vector v;
    do{
        cout<<"\nMenu"<<endl<<"1. Create vector\t2. Modify Vector\n3. Multiply by scalar\t4. Display vector"<<endl;
        cout<<"Your choice: ";
        cin>>opt;
        cout<<endl;
        switch(opt){
            case 1: v.createVect();
                    break;
            case 2: v.modifyVect();
                    break;
            case 3: v.multiplyByScalar();
                    break;
            case 4: v.displayVect();
                    break;
            default: "Invalid choice!";      
        }
        cout<<"Would you like to continue? (y/n): ";
        cin>>ch;
    }while (ch=='y'||ch=='Y');
    return 0;
}