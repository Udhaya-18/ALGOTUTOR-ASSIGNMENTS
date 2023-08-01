
#Valid Anagram

def isAnagram(self, s: str, t: str) -> bool:
        l1=[0 for i in range(26)]
        l2=[0 for i in range(26)]
        s1=len(s)
        s2=len(t)
        if(s1==s2):
            for i in range(len(s)):
                l1[ord(s[i])-ord('a')]+=1
                l2[ord(t[i])-ord('a')]+=1
            for i in range(26):
                if l1[i]!=l2[i]:
                    return False
            return True
        else:
            return False