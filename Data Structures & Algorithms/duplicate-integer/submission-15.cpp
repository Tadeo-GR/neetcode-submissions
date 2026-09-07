class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {  // <-- Renamed from containsDuplicate
        unordered_set<int> seen;
        for (int num : nums) {
            if (seen.find(num) != seen.end()) return true;
            seen.insert(num);
        }
        return false;
    }
};