SOLUTION = class Solution {
public:
   int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
       int total = 0, tank = 0, start = 0;

       for (int i = 0; i < gas.size(); i++) {
           total += gas[i] - cost[i]; // Calculate total gas available
           tank += gas[i] - cost[i];  // Track current tank level

           if (tank < 0) {  // If tank becomes negative, reset starting point
               start = i + 1;
               tank = 0;
           }
       }

       return total >= 0 ? start : -1; // If total gas is sufficient, return starting point, otherwise -1
   }
};
