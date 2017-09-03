import random
class RandomizedSet(object):
  def __init__(self):
    self.nums = []
    self.pos = {}

  def insert(self, val):
    if val in self.pos:
      return False

    self.nums.append(val)
    self.pos[val] = len(nums) - 1
    return True

  def remove(self, val):
    if val not in self.pos:
      return False
    # 找到要删除的val的index和nums的最后一项
    index, last = self.pos[val], self.nums[-1]
    # 找到nums的val然后换成nums最后一项, 最后一项的坐标变成index
    self.nums[index], self.pos[last] = last, index
    self.nums.pop()
    self.pos.pop(val)
    return True

  def getRandom(self):
    return self.nums[random.randint(0, len(self.nums) - 1)]
    
