class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        s = ""
        for i in strs:
            l = len(i)
            s += str(l)+"#"+i
        return s

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res = []
        i = 0
        while i < len(str):
            l = ''
            while str[i] != '#':
                l += str[i]
                i += 1
            intLength = int(l)
            i += 1
            res.append(str[i:i+intLength])
            i = i+intLength
        return res
