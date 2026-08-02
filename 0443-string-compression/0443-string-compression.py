class Solution:
    def compress(self, chars: List[str]) -> int:
        ins,i=0,0
        while i<len(chars):
            group=1
            while (group+i)<len(chars) and chars[group+i]==chars[i]:
                group+=1
            chars[ins]=chars[i]
            ins+=1
            if group>1:
                string=str(group)
                chars[ins:ins+len(string)]=list(string)
                ins+=len(string)
            i+=group
        return ins


        