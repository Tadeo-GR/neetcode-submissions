class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Try every pair (i, j) where i < j
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};  // Found the pair!
                }
            }
        }
        // According to the problem, we always find a solution
        return new int[]{-1, -1}; // Should never reach here (but required for compilation)
    }
} 