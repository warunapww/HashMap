import random
from typing import List, Tuple

class HashMap:
  """HashMap based on Cuckoo hashing
     This implementation only supports two maps/tables
  """
  def __init__(self, capacity: int = 30, load_factor: float = 0.5):
    """Initializes the hashmap with `capacity` and the `load_factor`. 
       If the load factor becomes higher than the provided value,
       the hashmap will be resized. 

       The load_factor = number of key, value pairs in the map / capacity of the map
    """
    self.capacity = capacity
    self.load_factor = load_factor

    self.number_of_tables = 2
    self.number_of_tries = 2 * self.number_of_tables + 1  # number of attempts to insert a key, value pair
    
    self.size = 0 # The number of key, value pairs stored in the map
    self._map=[[None] * self.capacity for _ in range(self.number_of_tables)]

    ##defining hash functions based on universal hash
    self.p = 2**61 - 1  # Prime number close to 2^64
    self.a, self.b = self._create_new_hash_params()

    #print(self.a)
    #print(self.b)


  def get(self, key: str) -> int | None:
    """Returns the `value` corresponds to the provided `key`, 
       or `None` if the `key` does not contain in the HashMap
    """
    for table_index in range(self.number_of_tables):
      hash_val = self._hash(key, table_index)
      table = self._map[table_index]
  
      if table[hash_val] is not None:
          k, v = table[hash_val]
          if k == key:
              return v

    return None

  def set(self, key: str, value: int) -> None:
    """Add the `key`, `value` pair if it does not exist in the HashMap, or
       update the `value` if the `key` already exists in the HashMap. 
    """
    if self.size / self.capacity > self.load_factor:
      #print(self._map)
      self._resize(self.capacity * 2)
      
    # update the key, value pair if the key already in the table
    for table_index in range(self.number_of_tables):
      hash_val = self._hash(key, table_index)
      table = self._map[table_index]

      if table[hash_val] is not None:
        if table[hash_val][0] == key:
          #print("NN {0} - {1}".format(table_index, hash_val))
          table[hash_val] = (key, value)
          return

    try_count = 0 
    # try max self.number_of_tries to find a location for the key value pair 
    #for i in range(self.number_of_tries):
    while try_count < self.number_of_tries:
      #print("try {0}".format(try_count))
      
      # outer iteration over the tables 
      # this loop make sure for each evicted pair,
      # first we check if a location is available on another table
      for table_outer_index in range(self.number_of_tables):
        #print("OI {0}".format(table_outer_index))
      
        # Insert the key value pair if the location is empty
        for table_index in range(self.number_of_tables):
          # in previous iteration we already checked it
          if table_index == table_outer_index - 1:
            continue
          hash_val = self._hash(key, table_index)
          table = self._map[table_index]

          if table[hash_val] is None:
            #print("N {0} - {1}".format(table_index, hash_val))
            table[hash_val] = (key, value)
            self.size += 1
            return

        #for table_index in range(self.number_of_tables):
        hash_val = self._hash(key, table_outer_index)
        table = self._map[table_outer_index]
        (key, value), table[hash_val] = table[hash_val], (key, value)
        try_count += 1

    # Increase the capacity of the tables and renew the hash functions
    self._resize(self.capacity * 2)

    #print(self._map)

    # Try to insert the evicted value again
    self.set(key, value)
    
    #print(self._map)
    

  def delete(self, key: str) -> None:
    """Remove the `key`, value pair from the HashMap, if it exists
    """
    for table_index in range(self.number_of_tables):
      hash_val = self._hash(key, table_index)
      table = self._map[table_index]
  
      if table[hash_val] is not None:
        k, v = table[hash_val]
        if k == key:
          table[hash_val] = None
          self.size -= 1
          return

  def _universal_hash(self, key: str, table_idx: int, capacity: int, a: List[int], b: List[int]) -> int: 
    return ((a[table_idx] * hash(key) + b[table_idx]) % self.p) % capacity

  def _hash(self, key: str, table_idx: int = 0, capacity: int = 0, a: List[int] = None, b: List[int] = None) -> int:
    """Compute the hash of the provided `key`. 
    """
    capacity = self.capacity if capacity == 0 else capacity
    a = self.a if a == None else a
    b = self.b if b == None else b
    return self._universal_hash(key, table_idx, capacity, a, b)

  def _create_new_hash_params(self) -> Tuple[List[int], List[int]]:
    a = [ random.randint(1, self.p - 1) for _ in range(self.number_of_tables) ]
    b = [ random.randint(0, self.p - 1) for _ in range(self.number_of_tables) ]
    return (a, b)

  def _resize(self, new_capacity: int) -> None:
    #print("resizing")
    #print(self._map)
    new_map=[[None] * new_capacity for _ in range(self.number_of_tables)]
    new_a, new_b = self._create_new_hash_params()
    new_size = 0

    # reinsert data into the new hash map
    for table_idx in range(self.number_of_tables):    
      for idx, pair in enumerate(self._map[table_idx]):
        if pair is not None:
          key, value = pair
          """
          # try max self.number_of_tries to find a location for the key value pair
          for i in range(self.number_of_tries):
            
            # update the key, value pair if the key already in the table
            for table_index in range(self.number_of_tables):
              hash_val = self._hash(key, table_index, new_capacity, new_a, new_b)
              table = new_map[table_index]

              if table[hash_val] is not None:
                  if table[hash_val][0] == key:
                      table[hash_val] = (key, value)
                      return


            # Insert the key value pair if the location is empty
            for table_index in range(self.number_of_tables):
              hash_val = self._hash(key, table_index, new_capacity, new_a, new_b)
              table = new_map[table_index]

              if table[hash_val] is None:
                table[hash_val] = (key, value)
                new_size += 1
                return

            for table_index in range(self.number_of_tables):
              hash_val = self._hash(key, table_index, new_capacity, new_a, new_b)
              table = new_map[table_index]
              (key, value), table[hash_val] = table[hash_val], (key, value)

          """

          status, new_size = self._set(key, value, new_capacity, new_a, new_b, new_map, new_size)

          if not status:
            raise ValueError("Unable to insert the key, value pair during the resize operation. The number of retries exeeded")

    self.capacity = new_capacity
    self._map = new_map
    self.a = new_a
    self.b = new_b
    self.size = new_size

  def _set(self, key: str, value: int, new_capacity: int, new_a: List[int], new_b: List[int], new_map: List[List[Tuple[str, int]]], new_size: int) -> Tuple[bool, int]:
    # try max self.number_of_tries to find a location for the key value pair
    for i in range(self.number_of_tries):

      # update the key, value pair if the key already in the table
      for table_index in range(self.number_of_tables):
        hash_val = self._hash(key, table_index, new_capacity, new_a, new_b)
        table = new_map[table_index]

        if table[hash_val] is not None:
            if table[hash_val][0] == key:
                table[hash_val] = (key, value)
                return (True, new_size)
      
      # outer iteration over the tables
      # this loop make sure for each evicted pair,
      # first we check if a location is available on another table
      for table_outer_index in range(self.number_of_tables):

        # Insert the key value pair if the location is empty
        for table_index in range(self.number_of_tables):
          hash_val = self._hash(key, table_index, new_capacity, new_a, new_b)
          table = new_map[table_index]

          if table[hash_val] is None:
            table[hash_val] = (key, value)
            new_size += 1
            return (True, new_size)

        hash_val = self._hash(key, table_outer_index, new_capacity, new_a, new_b)
        table = new_map[table_outer_index]
        (key, value), table[hash_val] = table[hash_val], (key, value)

    return (False, new_size)
