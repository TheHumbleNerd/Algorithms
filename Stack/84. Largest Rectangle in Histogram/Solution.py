class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [] #(index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            startIndex = i
            while st and st[-1][1] > h:
                index, height = st.pop()
                maxArea = max(maxArea, height*(i-index))
                startIndex = index
            st.append((startIndex, h))
        
        for i, h in st:
            maxArea = max(maxArea, h*(len(heights) - i))

        return maxArea
