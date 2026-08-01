class Solution(object):
    def reverseOnlyLetters(self, s):
        s=list(s)
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.alpha(s[l]):
                l+=1
            while r>l and not self.alpha(s[r]):
                r-=1
            if l<r:
                s[l],s[r]=s[r],s[l]
                l,r=l+1,r-1
        return ''.join(s)


    def alpha(self,c):
        return (ord('a')<=ord(c)<=ord('z') or ord('A')<=ord(c)<=ord('Z'))

  
        
        
       