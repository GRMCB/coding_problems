"""
#### 🏢 Crusoe Business Context
Crusoe Cloud workloads are split into "Standard" and "Preemptible" tiers. Preemptible jobs are cost-efficient 
but are killed instantly if a Standard job needs the high-performance compute or server space. 

#### 📋 Problem Statement
You are given a list of already scheduled `standard_jobs` as sorted `[start, end]` intervals. 
You are also given a single long `preemptible_job` interval. Return a list of all time segments 
where the preemptible job can actually execute without getting interrupted.

#### 📥 Example Input
```python
standard_jobs = [[1, 3], [6, 8]]
preemptible_job = [0, 10]
```

#### 📤 Example Output
```python
[[0, 1], [3, 6], [8, 10]]
```
"""

from typing import List

class Solution:
    def standard_preemption_jobs(self, standard_jobs: List[List[int]], preemptible_job: List[int]) -> List[List[int]]:
        # 1. Sort standard jobs by start time
        standard_jobs.sort(key=lambda x: x[0])
        preemptible_start, preemptible_end = preemptible_job
        valid_slots = []
        current_time = preemptible_start
        
        for start, end in standard_jobs:
            # If the standard job starts after our preemptible job ends, we are done
            if start >= preemptible_end:
                break
                
            # If the standard job ends before our preemptible job even starts, skip it
            if end <= preemptible_start:
                continue
                
            # Add a valid gap if there's free time before this standard job starts
            if start > current_time:
                valid_slots.append([current_time, min(start, preemptible_end)])
            
            # Move our timeline forward, ensuring we don't move backward 
            # if a standard job started before preemptible_start
            current_time = max(current_time, end)
            
        # 2. Add any remaining free time at the end of the window
        if current_time < preemptible_end:
            valid_slots.append([current_time, preemptible_end])
            
        return valid_slots

# --- Testing the code ---
standard_preemption_jobs_solver = Solution()

standard_jobs = [[1, 3], [6, 8]]
preemptible_job = [0, 10]

jobs = standard_preemption_jobs_solver.standard_preemption_jobs(standard_jobs, preemptible_job)

# This will successfully print: [[0, 1], [3, 6], [8, 10]]
print(jobs)
