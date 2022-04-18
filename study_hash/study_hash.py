
class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

class hash_table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key):
        return key % self.capacity

    def add_node(self, key, value):
        hash_key = self.hash_value(key)     ## key를 hash table에 맞게 변환
        p = self.table[hash_key]            ## hash table내 첫번째 node 접근
        while p is not None:                ## 첫번째 node가 None이 아닌 경우
            if key == p.key:                ## 중복되는 key가 이미있는 경우
                return False
            p = p.next                      ## 다음 node 접근
        node = Node(key, value, self.table[hash_key])
        self.table[hash_key] = node
        return True

    def search_node(self, key):
        hash_key = self.hash_value(key)
        p = self.table[hash_key]
        while p is not None:
            if key == p.key:
                return p.value
            p = p.next
        return False

    def remove_node(self, key):
        hash_key = self.hash_value(key)
        p = self.table[hash_key]
        previous_node = p
        while p is not None:
            if key == p.key:
                previous_node.next = p.next
                return True
            previous_node = p
            p = p.next
        return False

    def print_all_table(self):
        for i in self.table:
            while i is not None:
                print(i.value)
                i = i.next

if __name__ == "__main__":
    HanHashTable = hash_table(3)
    HanHashTable.add_node(4, 10)
    HanHashTable.add_node(7, 11)
    HanHashTable.add_node(1, 12)
    HanHashTable.print_all_table()
    number = HanHashTable.search_node(7)
    print(number)
    HanHashTable.remove_node(7)
    HanHashTable.print_all_table()