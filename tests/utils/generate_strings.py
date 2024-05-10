import random, string
from typing import List

def _random_word(length):
  """Return a string of size `length`. 
     String may contain any string printable characters
  """
  letters = string.printable
  #letters = string.digits+string.ascii_letters
  return ''.join(random.choice(letters) for i in range(length))

def _get_max(strLists: List[List[str]]) -> int:
  """Out of all the lists in the 
  """
  maxVal = 0
  for i in range(0, 30):
    maxVal = max(maxVal, len(strLists[i]))

  return maxVal

def strings_with_same_hash(count: int, hash_function) -> List[str]:
  """Return `count` number of strings with same hash value
  """

  strLists =[[] for _ in range(0,count)]

  # while the number of strings in atleast one list is less than 
  # the required number of strings, we keep on adding new strings
  while _get_max(strLists) < count:
    s = _random_word(random.randint(5, 5))
    strLists[hash_function(s)].append(s)

  for i in range(0, count):
    if len(strLists[i]) >= count:
      #print("index: {0}".format(i))
      return strLists[i]

def strings_with_unique_hash(count: int, hash_function) -> List[str]:
  """Return `count` number of strings with unique hash values
  """

  strList =[None for _ in range(0,count)]

  # while the number of strings in atleast one list is less than
  # the required number of strings, we keep on adding new strings
  while None in strList:
    s = _random_word(random.randint(5, 5))
    strList[hash_function(s)] = s

  #print(strList)

  return strList


if __name__ == '__main__':
    _hash = lambda key: hash(key) % 30
    #strings_with_same_hash(31, _hash)
    strings_with_unique_hash(30, _hash)

