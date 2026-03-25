class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size()<=2) return nums.size();

        int slow=1;
        int count=1;

        for (int i=1; i<nums.size(); i++){
            if( nums[i] == nums[i-1]) {
                count++;
            } else{
                count=1;
            }
            if(count<=2){
                nums[slow] = nums[i];
                slow++;
            }
        }
        return slow;
    }
};
