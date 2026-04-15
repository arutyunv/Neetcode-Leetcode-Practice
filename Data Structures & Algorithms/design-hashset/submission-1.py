"""

A little refresh of what HashSet is: 

A HashSet is a collection of unique values where we can:
1. Add fast 
2. Check existence fast 
3. Remove fast 

We don’t store elements randomly — we use a hash function to decide where to store them. 

Core Idea: Hashing. We use a function like: index = key % size. 
This maps any key to a position in an array. Example:
   * key = 1, so index = 1 % 1000 = 1
   * key = 1001 → index = 1001 % 1000 = 1
Problem: collisions (different keys - same index)

How to handle collisions? We use chaining: Each index stores a list (bucket)
So instead of: array[index] = key

We do: array[index] = [list of keys]
""" 


class MyHashSet:

    def __init__(self):
        self.size = 1000001 # number of buckets

        # Create an array of empty lists
        # Each list = a "bucket" that will hold multiple values if collisions happen
        self.data = [[] for _ in range(self.size)]  

    def hash(self, key):
        # Hash function: maps key -> index in array
        # % (mod) ensures index stays within [0, size-1]
        return key % self.size 

    def add(self, key: int) -> None:
        # Step 1: compute where this key should go
        index = self.hash(key) 
        # Step 2: get the bucket (list) at that index
        bucket = self.data[index]

        # Step 3: avoid duplicates (HashSet only stores unique values)
        if key not in bucket:
            # Step 4: insert key into bucket
            bucket.append(key)

    def remove(self, key: int) -> None:
        # Step 1: find bucket
        index = self.hash(key)
        bucket = self.data[index]

        # Step 2: only remove if it exists (to avoid errors)
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        # Step 1: find bucket
        index = self.hash(key)
        bucket = self.data[index]

        # Step 2: check if key exists inside that bucket
        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)