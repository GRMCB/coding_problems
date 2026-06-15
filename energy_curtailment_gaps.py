"""
#### 🏢 Business Context
When wind farms generate more energy than the power grid can accept, they enter a state called "curtailment" (wasted power). Company A hooks up data centers to eat up this excess energy. 
To track system utilization, engineers need to find the specific intervals when no turbines were experiencing curtailment.

#### 📋 Problem Statement
You are given a list of `curtailment_intervals` from multiple wind turbines sorted by start time. Find and return the time intervals when no turbines were experiencing curtailment within a global operating day timeline of [0, 24].

#### 📥 Example Input
```python
curtailment_intervals = [[1, 3], [2, 6], [8, 10]]
```

#### 📤 Example Output
```python
[[0, 1], [6, 8], [10, 24]]
```
"""



from typing import List

class Solution:
    def energy_curltailment_gaps(self, intervals: List[int]) -> List[int]:
        gaps = []
        current_end = 0
        
        for start, end in intervals:
            if start > current_end:
                gaps.append([current_end, start])
            current_end = max(current_end, end)
            
        if current_end < 24:
            gaps.append([current_end, 24])
            
        return gaps


energy_curltailment_gaps = Solution()

gaps = energy_curltailment_gaps.energy_curltailment_gaps([[1, 3], [2, 6], [8, 10]])

print(gaps)