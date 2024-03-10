class TimeMap:

    def __init__(self):
        self.store = {} # key = str, value = list of tuples of type (str value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        val = (value, timestamp)
        if key not in self.store:
            self.store[key] = []
        self.store[key].append(val)

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])

        l, r = 0, len(values)-1
        while l <= r:
            m = l + ((r-l)//2)
            if timestamp == values[m][1]:
                result = values[m][0]
                break
            elif timestamp > values[m][1]:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
