class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.store.get(key):
            self.store.setdefault(key,[(value,timestamp)])
        self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.store.get(key):
            return ""
        sortedTimeValues = self.store.get(key)
        left,right = 0,len(sortedTimeValues) - 1
        currentValue = ""
        while left <= right:
            m = left + ((right - left) // 2)
            pivot = sortedTimeValues[m]
            if (timestamp == pivot[1]):
                return pivot[0]
            if timestamp < pivot[1]:
                right = m - 1
            else:
                currentValue = pivot[0]
                left = m + 1
        return currentValue
    
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)  
print(timeMap.get("foo", 1)  )       
print(timeMap.get("foo", 3))         
timeMap.set("foo", "bar2", 4) 
print(timeMap.get("foo", 4))    
print(timeMap.get("foo", 5))    



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)