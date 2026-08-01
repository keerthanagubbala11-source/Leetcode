class MyHashMap:

    def __init__(self):
        self.arr = []
        
    def put(self, key: int, value: int) -> None:
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
                self.arr[i][1] = value
                break
        else:
            self.arr.append([key,value])
   
    def get(self, key: int) -> int:
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
                return self.arr[i][1]
        return -1

    def remove(self, key: int) -> None:
        rem = -1
        for i in range(len(self.arr)):
            if self.arr[i][0] == key:
                rem = i
        if rem != -1:
            self.arr.pop(rem)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)