"""
#### 🏢 Business Context
Data center cooling efficiency is critical. Company A's monitoring systems model server racks as a binary hierarchy of network switches and physical nodes. 
To catch overheating zones quickly, you need to calculate the average temperature reading across each tier or horizontal level of the device tree.

#### 📋 Problem Statement
Given the root of a binary tree where each node's value represents a real-time thermal sensor reading in Celsius, 
return an array containing the average temperature value of the nodes at each level.

#### 📥 Example Input
```text
       30
      /  \
    15    20
   /  \
  8    12
```

#### 📤 Example Output
```python
[30.0, 17.5, 10.0]
```

"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def average_thermal_output(self, root: Optional[TreeNode]) -> List[float]:
        # Maps level_index -> [sum_of_temperatures, count_of_nodes]
        level_data = {}
        
        # Helper function to traverse the tree recursively
        def dfs(node: Optional[TreeNode], level: int):
            if not node:
                return
            
            # If this is the first time seeing this level, initialize it
            if level not in level_data:
                level_data[level] = [0.0, 0]
                
            # Update the sum and the node count for the current level
            level_data[level][0] += node.val
            level_data[level][1] += 1
            
            # Recursively visit children, moving down to the next level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        # Start DFS traversal from the root at level 0
        dfs(root, 0)
        
        # Compute the final averages from the collected data
        result = []
        for level in sorted(level_data.keys()):
            level_sum, level_count = level_data[level]
            result.append(level_sum / level_count)
            
        return result

# --- Helper function to turn a LeetCode-style list into a real binary tree ---
def build_tree_from_list(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes or nodes[0] is None:
        return None
        
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):
        curr = queue.popleft()
        
        # Build left child
        if i < len(nodes) and nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        
        # Build right child
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
        
    return root

# --- Execution ---

# 1. Turn your raw list into linked TreeNode objects
input_list = [30, 15, 20, 8, 12, None, None]
tree_root = build_tree_from_list(input_list)

# 2. Instantiate your solution and run the logic
average_thermal_output = Solution()
averages = average_thermal_output.average_thermal_output(tree_root)

# 3. Print the final result
print(averages)
