class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Edge case: empty or null array → no duplicates
        if (nums == null || nums.length == 0) {
            return false;
        }

        HashSet<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;      // duplicate found
            }
            seen.add(num);        // remember this number
        }
        return false;             // no duplicates
    }
}
