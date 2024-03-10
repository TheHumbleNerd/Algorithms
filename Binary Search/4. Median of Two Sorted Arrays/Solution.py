class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a
        
        totalLength = len(a) + len(b)
        halfLength = totalLength // 2

        result = float('-inf')
        l, r = 0, len(a)-1
        while True:
            i = l + ((r-l)//2)
            j = halfLength - i - 2

            ALeft = a[i] if i >= 0 else float('-infinity')
            BLeft = b[j] if j >= 0 else float('-infinity')
            ARight = a[i+1] if (i+1) < len(a) else float('infinity')
            BRight = b[j+1] if (j+1) < len(b) else float('infinity')

            if ALeft <= BRight and BLeft <= ARight:
                if totalLength%2 == 0:
                    result = (max(ALeft, BLeft) + min(ARight, BRight)) / 2
                else:
                    result = min(ARight, BRight)
                break
            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1
        
        return result
