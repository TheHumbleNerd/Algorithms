class Solution:
    def trap(self, height: List[int]) -> int:
        lMax = [0]
        rMax = [0]

        for i in range(1, len(height)):
            lMax.append(max(lMax[-1], height[i-1]))
        
        for i in range(len(height)-2, -1, -1):
            rMax.append(max(rMax[-1], height[i+1]))
        rMax.reverse()

        rainWater = 0
        for i, h in enumerate(height):
            leftM = lMax[i]
            rightM = rMax[i]
            waterCeil = min(leftM, rightM)
            if waterCeil > h:
                rainWater += waterCeil - h
        
        return rainWater
