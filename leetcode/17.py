#coding: utf8

# 17. 电话号码的字母组合

import copy

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        i_str = {"2": "abc", "3": "def", "4": "ghi",
                 "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        rst = ['']

        for i in digits:
            ret = []
            for r in rst:
                for s in i_str[i]:
                    ret.append(r+s)

            rst = ret

        return rst


print Solution().letterCombinations("23")