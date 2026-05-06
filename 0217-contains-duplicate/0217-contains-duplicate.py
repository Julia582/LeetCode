class Solution(object):
    def containsDuplicate(self, nums):
        Set=set()
        for n in nums:
          if n in Set:
            return True
          Set.add(n)
        return False
        