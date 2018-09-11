class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        word = ""
        cnt = 0
        z_ord = ord("0")
        n_ord = ord("9")
        before_cnt = 1
        
        for c in s:
            ord_c = ord(c)
            if c=="[":
                stack.append([cnt, word])
                cnt = 0
                word = ""
            elif c=="]":
                for _ in range(stack[-1][0]):
                    stack[-1][1] += word
                
                word = stack.pop()[1]
                
            elif ord_c<z_ord or ord_c>n_ord:
                word += c
            else:
                cnt = 10*cnt + int(c)
        
        return word
