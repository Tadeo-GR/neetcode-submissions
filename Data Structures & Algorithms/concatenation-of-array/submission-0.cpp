class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans = nums;                     // 1
        ans.insert(ans.end(), nums.begin(), nums.end()); // 2
        return ans;                                 // 3
    }
};