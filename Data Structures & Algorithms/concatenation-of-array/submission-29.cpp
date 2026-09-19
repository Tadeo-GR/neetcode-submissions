#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n=nums.size();
        vector<int> duplicate(2 * n);
        for(int i ; i<nums.size() ; i++){
            duplicate[i] = nums[i];
            duplicate[i+n] = nums[i];
        }
        return duplicate;
    }
};
