class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = [] #(index, temp)
        result = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while st and st[-1][1] < t:
                index, temp = st.pop()
                result[index] = i - index
            st.append((i, t))
        return result
