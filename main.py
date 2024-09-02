from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Calculate the total amount of chalk needed for one full round
        total_chalk = sum(chalk)
        
        # Compute the effective amount of chalk left after full rounds
        effective_chalk = k % total_chalk
        
        # Iterate through the chalk array to find the student
        for i, chalk_needed in enumerate(chalk):
            if effective_chalk < chalk_needed:
                return i
            effective_chalk -= chalk_needed
        
        # This line is unreachable, but included to satisfy the function signature
        return -1

# Example usage
solution = Solution()
chalk1 = [5, 1, 5]
k1 = 22
print(solution.chalkReplacer(chalk1, k1))  # Output: 0

chalk2 = [3, 4, 1, 2]
k2 = 25
print(solution.chalkReplacer(chalk2, k2))  # Output: 1
