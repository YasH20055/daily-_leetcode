class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Stores seen numbers as keys and their indices as values
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # Check if the needed partner number has already been seen
            if complement in seen:
                return [seen[complement], index]
            
            # Keep track of the current number and its index
            seen[num] = index
            
        return [] # Return empty if no solution is found
