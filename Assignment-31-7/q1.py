# Roman to Integer

def romanToInt(self, s: str) -> int:
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        i=0
        res=0
        while i<len(s)-1:
            s1=dic[s[i]]
            s2=dic[s[i+1]]
            if s1<s2:
                res+=s2-s1
                i+=2
            else:
                res+=s1
                i+=1
        if i==len(s)-1:
            res+=dic[s[-1]]
        return res