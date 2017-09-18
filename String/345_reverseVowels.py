class Solution(object):
    def reverseVowels(self, s):
        d = ['a', 'e', 'i', 'o', 'u']
        r = list(s)
        left, right = 0, len(s) - 1
        while left < right:
          if r[left] not in d:
            left += 1
            continue
          if r[right] not in d:
            right -=1
            continue
          r[left], r[right] = r[right], r[left]
          left += 1
          right -= 1 
        return r
