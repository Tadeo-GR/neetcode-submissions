class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        map.reserve(strs.size());
        
        for (const string& s : strs) {
            int count[26] = {0};
            for (char c : s) count[c - 'a']++;
            
            string key;
            key.reserve(52);
            for (int i = 0; i < 26; ++i) {
                key += to_string(count[i]);
                key += '#';
            }
            map[key].push_back(s);
        }
        
        vector<vector<string>> result;
        result.reserve(map.size());
        for (auto& [k, v] : map) result.push_back(std::move(v));
        return result;
    }
};
