class Solution(object):
    def rob(self, nums):
        rob1,rob2=0,0
        for i in nums:
            current=max(rob1,rob2+i)
            rob2=rob1
            rob1=current
            
        return rob1