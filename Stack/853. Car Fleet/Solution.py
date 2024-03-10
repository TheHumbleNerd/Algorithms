class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ip = [(p, s) for p, s in zip(position, speed)]
        ip.sort(reverse = True)
        st = []

        for p, s in ip:
            time = (target - p)/s
            st.append(time)
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()
        
        return len(st)
