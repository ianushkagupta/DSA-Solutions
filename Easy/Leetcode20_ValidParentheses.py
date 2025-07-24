# https://leetcode.com/problems/valid-parentheses/description/
class Solution(object):
    def isValid(self, s):
        openBrac = ['(','{','[']
        closeBrac = [')','}',']']
        mapping = {')':'(', '}':'{', ']':'['}

        stack = []
        output = False

        for i in s:
            if i in openBrac:
                stack.append(i)
            else:
                if stack and stack[-1] == mapping[i]:
                    stack.pop()
                    output = True
                    continue
                else:
                    output = False
                    break

        if stack:
            output = False

        return output
