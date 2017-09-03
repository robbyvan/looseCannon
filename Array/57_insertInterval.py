class Solution(object):
  def insert(self, intervals, newInterval):
    res = []
    insertPos = 0
    for interval in intervals:
      if newInterval.start > interval.end:
        res.append(interval)
        insertPos += 1
      elif newInterval.end < interval.start:
        res.append(interval)
      else:
        newInterval.start = min(interval.start, newInterval.start)
        newInterval.end = max(interval.end, newInterval.end)
    results.insert(insertPos, newInterval)
    return results