# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Example 1:


# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# Example 2:


# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
 

# Constraints:

# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        if len(coordinates) == 2:
            return True
        slope = []
        initial = coordinates[0]
        coordinates = coordinates[1:]
        for point in coordinates:     
            dy = float(point[1]-initial[1])
            dx = float(point[0]-initial[0])
            if dx !=0 :
                slope.append(float(dy/dx))
        if len(set(slope)) <= 1:
            return True
        return False
            
        