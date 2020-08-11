'''
cs2420 Project 7 - Hash Map
Dana Doggett
Dec 9, 2019

I certify that I wrote all this code
'''



class HashMap():
    ''' This impements a dictionary structure using linear-probing '''
    INITIAL_SIZE = 8
    def __init__(self):
        ''' initializes an empty HashMap '''
        self.buckets = [None] * HashMap.INITIAL_SIZE
        self._size = 0

    def generate_hash(self, key):
        ''' generates a hash value from a key. Key must be a string '''
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        index = 42
        for letter in key:
            index += (ord(letter) * 787) + 29
        return index % len(self.buckets)

    def get(self, key, default=None):
        ''' returns the value associated with key. If key is not found, default is returned '''
        index = self.generate_hash(key)
        for _ in range(len(self.buckets)):
            if self.buckets[index] is None:
                return default
            if self.buckets[index][0] == key:
                return self.buckets[index][1]
            index += 1
            index %= len(self.buckets)
        return None

    def set(self, key, value):
        ''' associates value with key. If HashMap gets too full,
            this will rehash the exiting map '''
        index = self.generate_hash(key)
        for _ in range(len(self.buckets)):
            if self.buckets[index] is None:
                self.buckets[index] = (key, value)
                self._size += 1
                load_factor = self._size / len(self.buckets)
                if load_factor >= 0.80:
                    self.rehash()
                return
            if self.buckets[index][0] == key:
                self.buckets[index] = (key, value)
                return
            index += 1
            index %= len(self.buckets)

        raise RuntimeError("HashMap is unexpectedly full")

    def clear(self):
        ''' clears the HashMap '''
        self._size = 0

    def capacity(self):
        ''' returns the capacity of the Hashmap '''
        return len(self.buckets)

    def size(self):
        ''' returns the number of key-value pairs currently in the HashMap '''
        return self._size

    def keys(self):
        ''' returns a list of keys in the Hashmap '''
        return [item[0] for item in self.buckets if item is not None]   # pylint: disable=E1136

    def rehash(self):
        ''' doubles the size of the bucket-list and rehashes the
            current data into the new bucket-list '''
        old_buckets = self.buckets
        self.buckets = [None] * len(self.buckets) * 2
        self._size = 0

        for i in range(len(old_buckets)):   # pylint: disable=C0200
            if old_buckets[i] is not None:
                self.set(old_buckets[i][0], old_buckets[i][1])
