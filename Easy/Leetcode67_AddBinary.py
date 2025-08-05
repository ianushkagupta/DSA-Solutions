#https://leetcode.com/problems/add-binary/description/
class Solution(object):
    def addBinary(self, a, b):
        res = []
        carry = 0

        i = len(a) - 1
        j = len(b) - 1

        while i >=0 or j >=0 or carry:
            digit1 = int(a[i]) if i>=0 else 0
            digit2 = int(b[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry

            char = str(total % 2)
            res.append(char)

            carry = total // 2

            i -= 1
            j -= 1

        return "".join(reversed(res))


        