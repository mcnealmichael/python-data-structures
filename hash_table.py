class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [None] * size
        self.count = 0
        self.load_factor_limit = 0.7

    def hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def set(self, key, value):
        index = self.hash(key)
        if self.buckets[index] is None:
            bucket_list = []
            bucket_list.append((key, value))
            self.buckets[index] = bucket_list
            self.count += 1
        else:
            for i, pair in enumerate(self.buckets[index]):
                if pair[0] == key:
                    self.buckets[index][i] = (key, value)
                    return
            self.buckets[index].append((key, value))
            self.count += 1
        if self.count / self.size >= 0.7:
            self.resize()

    def get(self, key):
        index = self.hash(key)
        if self.buckets[index] is None:
            raise Exception("No key found")
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        raise Exception("No key found")

    def resize(self):
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [None] * self.size
        for bucket in old_buckets:
            if bucket is None:
                continue
            for (key, value) in bucket:
                new_index = self.hash(key)
                if self.buckets[new_index] is None:
                    new_bucket_list = []
                    new_bucket_list.append((key, value))
                    self.buckets[new_index] = new_bucket_list
                else:
                    self.buckets[new_index].append((key, value))

    def delete(self, key):
        index = self.hash(key)
        if self.buckets[index] is None:
            raise Exception("Key not found")
        for pair in self.buckets[index]:
            if pair[0] == key:
                self.buckets[index].remove(pair)
                self.count -= 1
                if not self.buckets[index]:
                    self.buckets[index] = None
                return
        raise Exception("Key not found")

my_hash_table = HashTable()
my_hash_table.set("cat", "meow")
my_hash_table.set("dog", "bark")
my_hash_table.set("act", "drama")
print(my_hash_table.get("cat"))
print(my_hash_table.get("dog"))
print(my_hash_table.get("act"))
my_hash_table.set("cat", "purr")
print(my_hash_table.get("cat"))
my_hash_table.delete("dog")
try:
    my_hash_table.get("dog")
    print("FAIL: no exception raised")
except Exception as e:
    print("PASS:", e)
print(my_hash_table.buckets[my_hash_table.hash("dog")] is None)
my_hash_table.delete("cat")
print(my_hash_table.get("act"))
bucket = my_hash_table.buckets[my_hash_table.hash("act")]
print(f"Count in the bucket is: {len(bucket)}")
try:
    my_hash_table.delete("nope")
    print("FAIL: no exception raised")
except Exception as e:
    print("PASS:", e)
my_other_hash_table = HashTable()
my_other_hash_table.set("cat", "meow")
my_other_hash_table.set("dog", "bark")
my_other_hash_table.set("act", "drama")
my_other_hash_table.set("car", "mercedes")
my_other_hash_table.set("motorcycle", "honda")
my_other_hash_table.set("truck", "freight")
my_other_hash_table.set("star", "sun")
my_other_hash_table.set("Musk", "tesla")
my_other_hash_table.set("Jobs", "apple")
my_other_hash_table.set("Engineer", "computer")
print(f"Table resized to: {my_other_hash_table.size}")
for bucket in my_other_hash_table.buckets:
    print(bucket)