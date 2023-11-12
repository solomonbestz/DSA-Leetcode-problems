import string
from typing import Any, Optional


class HashMap:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_key(self, key: str) -> int:
        hash_code = 0
        for char in key:
            hash_code += ord(char)
        return hash_code % self.MAX
    
    def __setitem__(self, key: Any, value: Any) -> None:
        hash_code = self.get_key(key)
        found_collision = False
        
        for index, element in enumerate(self.arr[hash_code]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash_code][index] = (key, value)
                found_collision = True
                break
        if not found_collision:
            self.arr[hash_code].append((key, value))


    def __getitem__(self, key: Any):
        hash_code = self.get_key(key)
        for element in self.arr[hash_code]:
            if self.arr[hash_code][element][0] == key:
                return self.arr[hash_code][element][1]
    

    def add(self, key, value):
        hash_code = self.get_key(key)
        self.arr[hash_code] = value

    # def get(self, key):
    #     hash_code = self.get_key(key)
    #     return self.arr[hash_code] if self.arr[hash_code] is not None else "Key Not Found"
    


if __name__=='__main__':
    # print([ord(char) for char in string.ascii_letters])
    hash_map = HashMap()
    hash_map.add("may12", 20000)
    hash_map.add("june17", 459)
    hash_map.add("may12", 20056)
    print(hash_map.arr)


    print(hash_map["may12"])
