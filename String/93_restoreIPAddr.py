class Solution(object):
  def restoreIpAddresses(self, s):
    # if len(s) > 12 or len(s) < 4:
    #   return []
    res = []
    self.helper(s, 0, "", 0, res)
    return res

  def helper(self, ip, index, restored, count, res):
    if count > 4:
      return
    if count == 4 and index == len(ip):
      res.append(restored)
    for offset in range(1, 4):
      if index + offset > len(ip):
        break
      s = ip[index:index + offset]
      if (s and s[0] == '0' and len(s) > 1):
        continue
      if offset == 3 and int(s) > 255:
        continue
      gen = restored + s + '.' if count < 3 else restored + s
      self.helper(ip, index + offset, gen, count + 1, res)
