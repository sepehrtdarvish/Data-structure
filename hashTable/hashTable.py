import math

class HashTable():
    HASH_METHODES = {'D': 'devision', 'M': 'multiplication'}
    COLLISION_METHODES = {'CH': 'chaining', 'lp': 'linear_probing', 'qp': 'quadratic_probing'}
    DEFAULT_DEMICAL_COEFFICIENT = 0.6180339887
    
    
    def __init__(self, hash_method, collision_res_method, size):
        self.hash_function = self.hash_function_factory(hash_method=hash_method)
        self.insert_function = self.collision_res_methods_factory(collision_res_method=collision_res_method)
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function_factory(self, hash_method):
        if hash_method not in self.HASH_METHODES.keys():
            raise Exception('Invalid Hash method! (D For devision, M For multiplication)')
        elif hash_method == 'D':
            return self.devision_hash
        elif hash_method == 'M':
            return self.multiplication_hash

    def collision_res_methods_factory(self, collision_res_method):
        if collision_res_method not in self.COLLISION_METHODES.keys():
            raise Exception('Invalid Collision Resolution Methods! (CH For chaining, OA For open addressing)')
        elif collision_res_method == 'CH':
            return self.chaining_insert
        elif collision_res_method == 'lp':
            return self.linear_probing_insert
        elif collision_res_method == 'qp':
            return self.quadratic_probing_insert
        
    def insert(self, key ,value):
        hashed_key = self.hash_function(key=key)
        self.insert_function(hashed_key=hashed_key,key=key, value=value)

    def devision_hash(self, key):
        return key % self.size
    
    def multiplication_hash(self, key, decimal_coefficient = None):
        if not decimal_coefficient:
            decimal_coefficient = self.DEFAULT_DEMICAL_COEFFICIENT

        mult_hash_function = lambda k: int(self.size * ((k*decimal_coefficient) % 1))
        
        return mult_hash_function(key)
    
    def chaining_insert(self, hashed_key, key, value):
        self.table[hashed_key].append([key, value])

    def linear_probing_insert(self, hashed_key, key, value):
        for i in range(self.size):
            idx = (hashed_key + i) % self.size
            if len(self.table[idx]) == 0:
                self.table[idx] = [[key, value]]
                return
        raise Exception("Hash table is full!")

    def quadratic_probing_insert(self, hashed_key, key, value):
        for j in range(self.size):
            idx = (hashed_key + j**2) % self.size
            if len(self.table[idx]) == 0:
                self.table[idx] = [[key, value]]
                return
        raise Exception("Hash table is full!")

    def display(self):
        """Display the contents of the hash table."""
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")


hash_table = HashTable(hash_method='D', collision_res_method='qp', size=20)
hash_table.insert(key=4, value='ali')
hash_table.insert(key=45, value='sep')
hash_table.insert(key=48, value='sep')
hash_table.insert(key=44, value='dachali')


hash_table.display()