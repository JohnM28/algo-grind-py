from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        k_sum = sum(nums[:k])
        best = k_sum
        for i in range(k, len(nums)):
            k_sum = k_sum - nums[i - k] + nums[i]
            if k_sum > best:
                best = k_sum
        return best

    def maximumSubarraySumWithDistinct(self, nums: List[int], k: int) -> int:
        k_sum, best = sum(nums[:k]), 0
        num_freq = {}
        for i in range(k):
            num_freq[nums[i]] = num_freq.get(nums[i], 0) + 1
        if len(num_freq) == k:
            best = k_sum
        for i in range(k, len(nums)):
            k_sum = k_sum - nums[i - k] + nums[i]
            num_freq[nums[i]] = num_freq.get(nums[i], 0) + 1
            num_freq[nums[i - k]] = num_freq.get(nums[i - k], 0) - 1
            if num_freq[nums[i - k]] == 0:
                del num_freq[nums[i - k]]
            if len(num_freq) == k and k_sum > best:
                best = k_sum
        return best


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 2, 9),  # Subarray [4, 5]
        ([1, -1, 5, -2, 3], 3, 6),  # Subarray [5, -2, 3]
        ([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3, 16),  # Subarray [7, 8, 1]
        ([1, 2, 3, 4, 5], 1, 5),  # Subarray [5]
        ([1, 2, 3, 4, 5], 5, 15)  # Subarray [1, 2, 3, 4, 5]
    ]

    for nums, k, expected in test_cases:
        result = solution.maximumSubarraySum(nums, k)
        print(f"maximumSubarraySum({nums}, {k}) = {result}, expected = {expected}")

    test_cases = [
        ([9, 9, 9, 1, 2, 3], 3, 12),  # Subarray [9 ,1 ,2]
        ([1, 2, 2, 3, 4], 3, 9),  # Subarray [2, 3, 4]
        ([1, 2, 3, 4, 5], 1, 5),  # Subarray [5]
        ([1, 2, 3, 4, 5], 5, 15),  # Subarray [1, 2, 3, 4, 5]
        ([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3, 16),  # Subarray [7, 8, 1]
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, 30),  # Subarray [6, 7, 8, 9]
        ([1, 2, 3, 1, 2, 3, 4, 5], 3, 12)  # Subarray [3, 4, 5]
    ]

    for nums, k, expected in test_cases:
        result = solution.maximumSubarraySumWithDistinct(nums, k)
        print(f"maximumSubarraySumWithDistinct({nums}, {k}) = {result}, expected = {expected}")
