import unittest
from hashmap import HashMap

class TestHashMap(unittest.TestCase):
  """Unit tests for HashMap
  """

  def test_create(self):
    map = HashMap()
    self.assertIsNotNone(map)
    self.assertEqual(map.capacity, 30)

  def test_insert(self):
    map = HashMap()
    key = "key1"
    value = 99
    map.set(key, value)
    val = map.get(key)
    self.assertEqual(value, val)

  def test_set(self):
    map = HashMap()
    key = "key1"
    value = 99
    map.set(key, value)
    value = 10
    map.set(key, value)
    val = map.get(key)
    self.assertEqual(value, val)

  def test_remove(self):
    map = HashMap()
    key = "key1"
    value = 99
    map.set(key, value)
    map.delete(key)
    val = map.get(key)
    self.assertIsNone(val)

  def test_get(self):
    map = HashMap()
    key = "key1"
    value = 99
    map.set(key, value)
    val = map.get(key)
    self.assertEqual(value, val)

  def test_hash(self):
    map = HashMap()
    index = map._hash("test1", 0)
    self.assertTrue(index < map.capacity and index >= 0)

if __name__ == '__main__':
    unittest.main()
