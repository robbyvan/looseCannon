class Solution(object):
  def compareVersion(self, v1, v2):
    version1 = self.trimRightZero(list(map(lambda x: int(x), v1.split('.'))))
    version2 = self.trimRightZero(list(map(lambda x: int(x), v2.split('.'))))
    for i in xrange(min(len(version1), len(version2))):
      if int(version1[i]) == int(version2[i]):
        continue
      elif int(version1[i]) > int(version2[i]):
        return 1
      return -1

    if len(version1) > len(version2):
      return 1
    elif len(version2) > len(version1):
      return -1
    return 0

  def trimRightZero(self, s):
    print(s)
    if len(s) == 0:
      return s
    while s[-1] == 0:
      s = s[0:-1]
      if len(s) == 0:
        break
    return s


