class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res+=str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:

        res,i = [],0
        while i < len(s):
            j = i
            while s[j]!="#":
                j +=1
            length = int(s[i:j]) #this is the integer

            res.append(s[j+1:j+1+length]) #index j+1 is at the 1st letter of the string, append all the letters till end of the string
            i=j+1+length #this is the index of the new string
        return res

