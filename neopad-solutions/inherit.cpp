#include <iostream>
#include <string>
using namespace std;
class Person {
protected:
    string name;
    int age;
public:
    void getPerson()
    {
            cout<<"ENter name and age: "<<endl;
            cin>>name>>age;
    }
};
class Student : public Person {
    int roll,marks;
public:
    void getStudent()
    {
            getPerson();
            cout<<"Enter rollno and marks: "<<endl;
            cin>>roll>>marks;
    }
    void display(){
        cout<<"Name: "<<name<<", Age: "<< age
             <<", Roll: "<<roll<<", Marks: "<<marks<<endl;
    }
};
int main(){
        Student p2;
        p2.getStudent();
        p2.display();
}
