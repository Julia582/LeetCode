class Solution(object):
    def reverseString(self, s):
        lp=0
        rp=len(s)-1
        while lp<rp:
            s[lp],s[rp]=s[rp],s[lp]
            lp = lp+1
            rp = rp-1
        