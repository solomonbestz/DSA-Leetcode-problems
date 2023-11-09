
from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monsters_killed = 0
        distance = len(dist)
        time = []
        
        for i in range(distance):
            time.append(round(dist[i] / speed[i], 2))

        time.sort()

        for distance in range(distance):
            if distance < time[distance]:
                monsters_killed += 1
            else:
                break 
        return distance if monsters_killed == distance else monsters_killed
    
if __name__=='__main__':
    war = Solution()
    print(war.eliminateMaximum([3,2,4], [5,3,2]))