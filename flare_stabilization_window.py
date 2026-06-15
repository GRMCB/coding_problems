"""
#### 📋 Problem Statement
Given an array of overlapping surge records `[start, end, volume]` and a threshold `K`, 
group the surges into continuous active generator windows. If overlapping surges have a combined volume less than `K`, 
the generator must power down at that point, breaking the window. Return the valid continuous operational intervals for the generator.

#### 📥 Example Input
```python
surges = [[1, 5, 10], [3, 7, 5]]
K = 12 
```

#### 📤 Example Output
```python
[[3, 5]]
```
"""

from typing import List

class Solution:
    def flare_stabilization_window(self, surges: List[int], K: int) -> List[int]:
        # 1. Break intervals into individual start/stop events
        events = []
        for start, end, vol in surges:
            events.append((start, vol))   # Vol goes up at start
            events.append((end, -vol))   # Vol goes down at end
            
        # 2. Sort all events by time chronologically
        events.sort(key=lambda x: x[0])
        
        stable_intervals = []
        current_volume = 0
        window_start = None
        
        # 3. Sweep through the timeline event by event
        i = 0
        while i < len(events):
            current_time = events[i][0]
            
            # Process all volume changes that happen at this exact timestamp
            # Needed or else overlapping windows could cause volume to drop below threshold k
            # when they should be seen in combination. 
            while i < len(events) and events[i][0] == current_time:
                current_volume += events[i][1]
                i += 1
                
            # If volume hits the threshold, note where the window starts
            if current_volume >= K and window_start is None:
                window_start = current_time
                
            # If volume drops below threshold, close the active window
            elif current_volume < K and window_start is not None:
                if current_time > window_start:
                    stable_intervals.append([window_start, current_time])
                window_start = None
                
        return stable_intervals


flare_stabilization_window = Solution()

window = flare_stabilization_window.flare_stabilization_window([[1, 5, 10], [3, 7, 5]], 12)

print(window)