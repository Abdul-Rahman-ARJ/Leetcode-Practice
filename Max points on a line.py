# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

# Example 1:


# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Example 2:


# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
 

# Constraints:

# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
                                                #   points = [[1,0],[2,1],[3,4], [5,4]]

        points.sort()                           #   point1 point2 (dx,dy)    m     slope                M
        slope, M = defaultdict(int), 0          #   –––––– –––––– ––––––– –––––––  –––––––––––        –––––
                                                #   [1,0]  [2,1]   (1,1)   (1,1)   {(1,1):1}            1
        for i, (x1, y1) in enumerate(points):   #          [3,4]   (2,4)   (1,2)   {(1,1):1,(1,2):1}    1
                                                #          [5,4]   (4,4)   (1,1)   {(1,1):2,(1,2):1}    2
            slope.clear()                       #   [2,1]  [3,4]   (1,3)   (1,3)   {(1,3):1}            2
                                                #          [5,4]   (3,3)   (1,1)   {(1,3):1,(1,1):1}    2
            for x2, y2 in points[i + 1:]:       #   [3,4]  [5,4]   (3,0)   (1,0)   {(1,0):1}            2
                dx, dy = x2 - x1, y2 - y1
                                                #  M + 1 = 2 + 1 = 3 <-- return
                G = gcd(dx, dy)                 
                m = (dx//G,dy//G)
                
                slope[m] += 1
                if slope[m] > M: M = slope[m]
    
        return M + 1
