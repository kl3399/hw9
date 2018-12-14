import random
import UnsortedArrayMap as unsorted_map

class ChainingHashTableMap:

    def __init__(self, N=64, p=40206835204840513073):
        self.N = N
        # self.table = [unsorted_map.UnsortedArrayMap() for i in range(self.N)]
        self.table = [None for i in range(self.N)]
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            return None
        elif isinstance(curr_bucket, unsorted_map.UnsortedArrayMap):
            return curr_bucket[key]
        else:
            return curr_bucket.value

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            old_size = 0
            new_item = unsorted_map.UnsortedArrayMap.Item(key, value)
            self.table[i] = new_item
            new_size = 1
        elif isinstance(curr_bucket, unsorted_map.UnsortedArrayMap):
            old_size = len(curr_bucket)
            curr_bucket[key] = value
            new_size = len(curr_bucket)
        else:
            old_size = 1
            new_bucket = unsorted_map.UnsortedArrayMap()
            new_bucket[curr_bucket.key] = curr_bucket.value
            new_bucket[key] = new_bucket.value
            self.table[i] = new_bucket
            new_size = 2
        if (new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            raise Exception("Bucket is none")
        elif isinstance(curr_bucket, unsorted_map.UnsortedArrayMap):
            del curr_bucket[key]
        else:
            self.table[i] = None
        self.n -= 1
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            if curr_bucket is not None:
                if isinstance(curr_bucket, unsorted_map.UnsortedArrayMap):
                    for key in curr_bucket:
                        yield key
                else:
                    yield curr_bucket.key

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val


def print_hash_table(ht):
    for i in range(ht.N):
        print(i, ": ", sep="", end="")
        curr_bucket = ht.table[i]
        for key in curr_bucket:
            print("(", key, ", ", curr_bucket[key], ")", sep="", end="")
        print()
