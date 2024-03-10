class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        lMax, rMax = height[i], height[j]
        rainWater = 0

        while i < j:
            if lMax < rMax:
                i += 1
                # if height[i] < lMax:
                #     rainWater += lMax - height[i]
                lMax = max(lMax, height[i])
                rainWater += lMax - height[i]
            else:
                j -= 1
                # if height[j] < rMax:
                #     rainWater += rMax - height[j]
                rMax = max(rMax, height[j])
                rainWater += rMax - height[j]
        
        return rainWater
