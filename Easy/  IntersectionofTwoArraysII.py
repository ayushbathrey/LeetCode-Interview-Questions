class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}  # Dictionary to store counts of elements in nums1
        output = []
        
        # Count occurrences of each number in nums1
        for num in nums1:
            res[num] = res.get(num, 0) + 1
        
        # Check for intersection with nums2
        for num in nums2:
            if num in res and res[num] > 0:
                output.append(num)
                res[num] -= 1  # Decrease the count in the dictionary
        
        return output