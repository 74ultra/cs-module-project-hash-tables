class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = 0

    def show_table(self):
        new_dict = {}
        for i in self.storage:
            e = i
            while e is not None:
                new_dict[e.key] = e.value
                e = e.next
        return new_dict

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def fnv1_f(self, key):
        fnv_prime = 1099511628211
        hash = 14695981039346656037
        for char in key:
            hash = hash * fnv_prime
            hash = hash ^ ord(char)
        return hash & 0xFFFFFFFFFFFFFFFF

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.check_size_up()

        node_ind = self.hash_index(key)
        if(self.storage[node_ind] == None):
            new_node = HashTableEntry(key, value)
            self.storage[node_ind] = new_node
            self.size += 1
            return
        else:
            current_node = self.storage[node_ind]
            while current_node is not None:
                if(current_node.key == key):
                    current_node.value = value
                    return
                elif(current_node.key != key and current_node.next is None):
                    new_node = HashTableEntry(key, value)
                    current_node.next = new_node
                    self.size += 1
                    return
                elif(current_node.key != key and current_node.next is not None):
                    current_node = current_node.next

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        node_ind = self.hash_index(key)
        current_node = self.storage[node_ind]
        prev_node = None

        while current_node is not None:
            if current_node.key == key:
                if prev_node is None:
                    self.storage[node_ind] = current_node.next
                    self.size -= 1
                    return
                else:
                    prev_node.next = current_node.next
                    self.size -= 1
                    return
            else:
                prev_node = current_node
                current_node = current_node.next
        print(f'The key "{key}" does not exist in this table.')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        node_ind = self.hash_index(key)
        for i in self.storage:
            e = i
            while e is not None:
                if e.key == key:
                    return e.value
                else:
                    e = e.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.show_table()
        self.capacity = new_capacity
        self.storage = [None] * self.capacity
        self.size = 0
        for i, j in old_table.items():
            self.put(i, j)
        print("upsized")

    def downsize(self, new_capacity):
        old_table = self.show_table()
        if new_capacity < 8:
            new_capacity = 8
        self.storage = [None] * self.capacity
        self.size = 0
        for i, j in old_table.items():
            self.put(i, j)
        print("downsized, capacity: ", self.capacity)

    def check_size_up(self):
        if self.size/self.capacity > 0.7:
            self.resize(self.capacity * 2)
        if (self.capacity > 8) and ((self.size/self.capacity) < 0.2):
            self.downsize(self.capacity / 2)


# if __name__ == "__main__":
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")
xer = HashTable(8)

print('initial', xer.capacity)

xer.put('sky', 'blue')
xer.put('grass', 'green')

xer.put('dirt', 'brown')
xer.put('flamingo', 'pink')
xer.put('oxblood', 'red')
xer.put('pitch', 'black')
xer.put('ocean', 'blue')
xer.put('prison', 'orange')
xer.put('cornflower', 'blue')
xer.put('the color', 'purple')
xer.put('midnight', 'blue')
xer.put('asdf', 'asdf')
xer.put('fdsa', 'fdsa')
xer.put('zzz', 'zzz')
xer.put('aaa', 'bbb')
xer.put('ccc', 'ccc')
xer.put('ddd', 'ddd')
xer.put('eee', 'eee')

print('post-add', xer.capacity)

xer.delete('zzz')
xer.delete('aaa')
xer.delete('ccc')
xer.delete('ddd')
xer.delete('eee')
xer.delete('asdf')
xer.delete('fdsa')
xer.delete('the color')
xer.delete('ocean')

print('post-delete', xer.capacity)


# print(' ')

# print(xer.show_table())
# print(xer.size)
