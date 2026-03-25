SOLUTION = class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> seen;

        while (n != 1 && !seen.count(n)) {
            seen.insert(n); // Track seen numbers to detect cycles
            int next = 0;
            while (n > 0) {
                int digit = n % 10;
                next += digit * digit;
                n /= 10;
            }
            n = next; // Update n for the next iteration
        }

        return n == 1; // Happy if it reaches 1, otherwise stuck in a cycle
    }
};
