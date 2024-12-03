class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge case for empty array

        # Initialize the slow pointer `k`
        k = 0

        for i in range(1, len(nums)):
            # If the current element is not equal to the last unique element
            if nums[i] != nums[k]:
                k += 1  # Move the `k` pointer forward
                nums[k] = nums[i]  # Update the next unique position with the new value

        # Return the length of the unique elements
        return k + 1