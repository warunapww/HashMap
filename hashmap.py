class HashMap:
  """HashMap with separate chaining
  """
  def __init__(self, size: int = 30):
    """Initializes the hashmap with `size` number of buckets
    """
    self.size = size
    self._map = [[] for _ in range(self.size)]

  def get(self, key: str) -> int | None:
    """Returns the `value` corresponds to the provided `key`, 
       or `None` if the `key` does not contain in the HashMap
    """
    index = self._hash(key)
    bucket = self._map[index]

    for (k, v) in bucket:
      if k == key:
        return v
  
    return None

  def set(self, key: str, value: int) -> None:
    """Add the `key`, `value` pair if it does not exist in the HashMap, or
       update the `value` if the `key` already exists in the HashMap. 
    """
    index = self._hash(key)
    bucket = self._map[index]

    for i, (k, v) in enumerate(bucket):
      if k == key:
        bucket[i]=(key, value)
        return

    bucket.append((key, value))

  def delete(self, key: str) -> None:
    """Remove the `key`, value pair from the HashMap, if it exists
    """
    index = self._hash(key)
    bucket = self._map[index]

    for i, (k, v) in enumerate(bucket):
      if k == key:
        del bucket[i]
        return

  def _hash(self, key: str) -> int:
    """Compute the hash of the provided `key`. 
    """
    return hash(key) % self.size

