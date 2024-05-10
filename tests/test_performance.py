import unittest
import time
import random
from hashmap import HashMap
import tests.utils.generate_strings as generate_strings

class PerfTests(unittest.TestCase):
  """Performance tests for HashMap
  """

  def test_worstcase(self):
    """Performance of the HashMap when all the keys mapped to the same bucket/index
    """

    set_total_time=0.0
    set_min_time = float('inf')
    set_max_time = float('-inf')
    get_total_time=0.0
    get_min_time = float('inf')
    get_max_time = float('-inf')
    count = 1000

    for _ in range(count):
      map = HashMap()
      keys = generate_strings.strings_with_same_hash(map.capacity, map._hash)

      ##print(keys)

      #shuffled_keys = [keys[map.capacity-1]] * map.capacity
      shuffled_keys = keys.copy()
      random.shuffle(shuffled_keys)

      #print(keys)

      #start_time = time.perf_counter()
      start_time = time.process_time()
      # Insert keys
      for i, key in enumerate(keys):
        map.set(key, i)

      #print(map._map)

      end_time = time.process_time()
      #end_time = time.perf_counter()

      # Read value of the keys in random order
      for i, key in enumerate(keys):
        val = map.get(key)

      get_end_time = time.process_time()

      del map

      set_elapsed_time = end_time - start_time
      set_total_time += set_elapsed_time
      set_min_time = min(set_min_time, set_elapsed_time)
      set_max_time = max(set_max_time, set_elapsed_time)
      get_elapsed_time = get_end_time - end_time
      get_total_time += get_elapsed_time
      get_min_time = min(get_min_time, get_elapsed_time)
      get_max_time = max(get_max_time, get_elapsed_time)

      #print('Elapsed time: %.6f %e' % (set_elapsed_time, set_elapsed_time))

    #print(map._map)

    set_avg_time = set_total_time/count
    get_avg_time = get_total_time/count

    print('')
    print('Elapsed time in seconds (set - avg, min, max): %e %e %e' % (set_avg_time, set_min_time, set_max_time))
    print('Elapsed time in seconds (get - avg, min, max): %e %e %e' % (get_avg_time, get_min_time, get_max_time))

  def test_averagecase(self):
    """Performance of the HashMap when all the keys mapped to the unique buckets/indices
    """

    set_total_time=0.0
    set_min_time = float('inf')
    set_max_time = float('-inf')
    get_total_time=0.0
    get_min_time = float('inf')
    get_max_time = float('-inf')
    count = 1000

    for _ in range(count):
      map = HashMap()
      keys = generate_strings.strings_with_unique_hash(map.capacity, map._hash)
      #print(keys)
      shuffled_keys = keys.copy()
      random.shuffle(shuffled_keys)
      #print(keys)

      #start_time = time.perf_counter()
      start_time = time.process_time()
      # Insert keys
      for i, key in enumerate(keys):
        map.set(key, i)

      #print(map._map)

      end_time = time.process_time()
      #end_time = time.perf_counter()

      # Read value of the keys in random order
      for i, key in enumerate(keys):
        val = map.get(key)

      get_end_time = time.process_time()

      del map

      set_elapsed_time = end_time - start_time
      set_total_time += set_elapsed_time
      set_min_time = min(set_min_time, set_elapsed_time)
      set_max_time = max(set_max_time, set_elapsed_time)
      get_elapsed_time = get_end_time - end_time
      get_total_time += get_elapsed_time
      get_min_time = min(get_min_time, get_elapsed_time)
      get_max_time = max(get_max_time, get_elapsed_time)

      #print('Elapsed time: %.6f %e' % (set_elapsed_time, set_elapsed_time))

    #print(map._map)

    set_avg_time = set_total_time/count
    get_avg_time = get_total_time/count

    print('')
    print('Elapsed time in seconds (set - avg, min, max): %e %e %e' % (set_avg_time, set_min_time, set_max_time))
    print('Elapsed time in seconds (get - avg, min, max): %e %e %e' % (get_avg_time, get_min_time, get_max_time))

