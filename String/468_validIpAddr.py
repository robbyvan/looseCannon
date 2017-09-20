class Solution(object):
  def validIPAddress(self, IP):
    ipv4 = IP.split('.')
    ipv6 = IP.lower().split(':')
    isIPv4 = self.checkIPv4(ipv4)
    isIPv6 = self.checkIPv6(ipv6)
    if isIPv4:
      return "IPv4"
    if isIPv6:
      return "IPv6"
    return "Neither"

  def checkIPv4(self, ipv4):
    if len(ipv4) != 4:
      return False

    for w in ipv4:
      if not w or w[0] == "0" and len(w) > 1:
        return False
      allows = "0123456789"
      for ch in w:
        if ch not in allows:
          return False
      try:
        num = int(w)
        if num < 0 or num > 255:
          return False
      except:
        return False
    return True

  def checkIPv6(self, ipv6):
    if len(ipv6) != 8:
      return False
    allows = "0123456789abcdef"
    for w in ipv6:
      if len(w) == 0 or len(w) > 4 or (w[0] == "0" and len(w) > 4):
        return False
      for ch in w:
        if ch not in allows:
          return False
    return True

a = Solution().validIPAddress("2001:0db8:85a3:033:0:8A2E:0370:7334")
print(a)