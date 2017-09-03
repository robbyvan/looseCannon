class RandomizedCollection(object):
  def __init__(self):
    self.nums = []
    self.pos = collections.defaultdict(set)

  def insert(self, val):
    self.nums.append(val)
    self.pos[val].add(len(self.nums))
    return len(self.pos[val]) == 1

  def remove(self, val):
    if val not in self.pos:
      return False
    i, newVal = self.pos[val].pop(), self.nums[-1]
    
