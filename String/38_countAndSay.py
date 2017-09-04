class Solution(object):
  def countAndSay(self, n):
    prevWord = '1'
    for i in xrange(2, n + 1):
      curr = ''
      if len(prev) == 1:
        curr = '1' + prevWord
      else:
        prevChar = prevWord[0]
        counter = 1
        for j in xrange(1, len(prevWord)):
          if prevWord[j] == prevChar:
            counter += 1
          else:
            curr = curr + str(counter) + prevChar
            prevChar = prevWord[j]
            counter = 1
        if counter > 0:
          curr = curr + str(counter) + prevChar
      prevWord = curr
    return prevWord
