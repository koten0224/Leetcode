class MyHashMap(dict):
    def put(self, key: int, value: int) -> None:
        self[key]=value
    def get(self, key: int) -> int:
        try:return self[key]
        except:return -1
    def remove(self, key: int) -> None:
        try:del self[key]
        except:pass