#include <iostream>
#include <cstring>
using namespace std;
class StringOp {
    char str[100];
public:
    void setString(const char* s)
    {
       strcpy(str, s);
    }
    int getLength()
    {
       return strlen(str);
    }
    void reverse() {
        int n = getLength();
        for(int i=0;i<n/2;i++)
           swap(str[i],str[n-i-1]);
        cout<<"Reversed: "<<str<<endl;
    }
    bool isPalindrome() {
        int n=getLength();
         for(int i=0;i<n/2;i++){
            if (str[i]!=str[n - i - 1]) return false;
        }
        return true;
    }
};
int main(){
   StringOp a;
   char s[100];
   cin>>s;
   a.setString(s);
   cout<<"Length of the String: "<<a.getLength()<<endl;
   a.reverse();
   cout<<"Palindrome is: ";
   bool b=a.isPalindrome();
   if (b==true){
      cout<<"It is Palindrome"<<endl;
   }
   else{
      cout<<"Not a palindrome"<<endl;
   }
}
