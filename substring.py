import math
class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = math.pow(10, 9) + 7
        res = 0
        pre = s[0]
        count = 0

        for i in range(len(s)):
            cur = s[i]
            if cur == pre:
                count += 1
            else:
                res += (count + 1) * count / 2
                count = 1
                pre = cur
        
        res += (count + 1) * count / 2
        return int(res % mod)



if __name__=='__main__':
    sub = Solution()
    print(sub.countHomogenous("abbcccaa"))

