from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node)->None:
        self.key = key
        self.value = value
        self.next = next

class ChaineHash:

    def __init__(self, capacity: int)-> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any):
        if isinstance(key, int):
            return key % self.capacity

        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16)%self.capacity)

    def search(self, key: Any)-> Any:
        hash = self.hash_value(key) # 검색하는 키의 해시값
        p = self.table[hash]        # 노드를 주목

        while p is not None:        #
            if p.key == key:
                return p.value
            p = p.next
        return None

    def add(self, key: Any, value: Any)-> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True