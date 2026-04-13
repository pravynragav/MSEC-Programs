#include <iostream>
using namespace std;

int productOfDigits(int n) {
    // Base Case: if the number is a single digit
    if (n < 10) {
        return n;
    }
    // Recursive Case: last digit * product of remaining digits
    return (n % 10) * productOfDigits(n / 10);
}
int main() {
    int n;
    cin >> n;  // Read the input number
    
    int result = productOfDigits(n);  // Call the recursive function to calculate the product
    cout << result << endl;  // Print the final product
