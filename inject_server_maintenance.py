"""
🏢 Business Context
A Crusoe Digital Flare Mitigation (DFM) system has a strict timeline of locked-in computing jobs. A new urgent security update must be scheduled. You need to insert this new maintenance window into the current schedule and merge it with any existing jobs that it disrupts, ensuring no computing time is double-allocated.

📋 Problem Statement
You are given an array of non-overlapping time intervals intervals sorted by their start time, where intervals[i] = [start, end] represents the busy times. You are also given a new_interval representing the maintenance window. Insert new_interval into intervals such that the schedule is still sorted and non-overlapping (merge overlapping intervals if necessary).

📥 Example Input
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]

📤 Example Output
[[1, 5], [6, 9]]

Explanation: The new interval [2, 5] overlaps with [1, 3], expanding the first operational block to [1, 5].
"""

from typing import List

class Solution:
    def inject_server_maintenance(self, intervals: List[int], new_interval: List[int]) -> List[int]:
        intervals.append(new_interval)
        intervals.sort(key=lambda x: x[0])
        merged = []
        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(interval[1], prev[1])
            else:
                merged.append(prev)
                prev = interval
        
        merged.append(prev)

        return merged

inject_server_maintenance = Solution()

merged = inject_server_maintenance.inject_server_maintenance([[1, 3], [6, 9]], [2, 5])

print(merged)