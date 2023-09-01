class Solution:
    def findLenOfSubString(self, s:str) -> int:
        #Initialize
        lst = []
        max = 0
        t_len = len(s)
        st = 0
        ed = 0
        lent = 0

        while (t_len > 0 and t_len-1 > ed):
            if(st == ed):
                lst.append(s[st])
                lent = 1
                ed +=1
            else:
                if s[ed] in lst:
                    #if element repeated then
                    #re-initialize
                    st += 1
                    ed = st
                    lst = []
                    lent = 0
                else:
                    #push element if not repeated
                    lst.append(s[ed])
                    lent += 1
                    ed += 1     
                    
            if(lent > max):
                max = lent
        return max
    

s1 = "abcabcbb"
s2 = "bbbb"
s3 = "pwwkew"
solutioin = Solution()
print(f"Max Length of {s1} is", solutioin.findLenOfSubString(s1))
print(f"Max Length of {s2} is", solutioin.findLenOfSubString(s2))
print(f"Max Length of {s3} is", solutioin.findLenOfSubString(s3))
