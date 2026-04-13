#include <iostream>
using namespace std;
class Student {
    int scores[5];
public:
    void input() {
        for(int i=0;i<5;i++) cin >> scores[i];
    }
    int totalScore() {
        int sum=0;
        for(int i=0;i<5;i++) sum+=scores[i];
        return sum;
    }
    bool operator>(Student s) {
        return this->totalScore() > s.totalScore();
    }
};
int main() {
    int n,count=0;
    cout<<"Enter n value:"<<endl;
    cin>>n;
    Student* s = new Student[n];
    for(int i=0;i<n;i++) s[i].input();
    for(int i=1;i<n;i++) {
        if(s[i]>s[0]) {
            count++;
        }
    }
    cout<<"Student scored more than 1 is: "<<count;
    delete[] s;
    return 0;
}
