#Reverse Words in a String

def reverseWords(self, s: str) -> str:
        li=s.strip().split(' ')
        print(li)
        li=[i for i in li if i!='']
        li.reverse()
        string = ' '.join([str(i) for i in li])
        return string