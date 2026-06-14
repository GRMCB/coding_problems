"""
### Business Context
A Company deploys mobile data centers directly to oil well sites to capture stranded natural gas 
that would otherwise be wasted or flared. Oil producers provide messy, 
overlapping schedules of when gas lines will be active. 
You must consolidate these overlapping time frames into absolute operational windows 
so the engineering team knows exactly when the generators must run continuously.

## Problem Statement
Given an array of gas flow time intervals intervals where intervals[i] = [start, end], 
merge all overlapping intervals. Return an array of the non-overlapping intervals 
that cover all the gas flow times in the input.
### Example Input

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
### Example Output
[[1, 6], [8, 10], [15, 18]]

Explanation: Intervals [1, 3] and [2, 6] overlap. They are merged into a single continuous window [1, 6].
"""
from typing import List

class Solution:
    def generator_schedule(self, intervals: List[int]) -> List[int]:
        prev = intervals[0]
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(interval[1], prev[1])
            else:
                merged.append(prev)
                prev = interval
        
        merged.append(prev)

        return merged

generator_schedule = Solution()

merged = generator_schedule.generator_schedule([[1, 3], [2, 6], [8, 10], [15, 18]])

print(merged)