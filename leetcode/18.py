#coding: utf8

'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断
nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''
import time

class Solution(object):
    def fourSum(self, nums, target=0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, dicti = set(), {}
        numLen = len(nums)
        nums.sort()
        for i in range(numLen):
            for j in range(i + 1, numLen):
                key = nums[i] + nums[j]
                if key not in dicti:
                    dicti[key] = [(i, j)]
                else:
                    dicti[key].append((i, j))

        for i in range(numLen):
            for j in range(i + 1, numLen - 2):
                exp = target - nums[i] - nums[j]
                if exp in dicti:
                    for tmpIndex in dicti[exp]:
                        if tmpIndex[0] > j:
                            res.add((nums[i], nums[j], nums[tmpIndex[0]], nums[tmpIndex[1]]))
        return [list(i) for i in res]



    def threeSum(self, nums, target=0):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r] - target
                    if s == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s > 0:
                        r -= 1
                    else:
                        l += 1
        return res

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            s = nums[l] + nums[r] - target
            if s == 0:
                return [nums[l], nums[r]]
            elif s > 0:
                r -= 1
            else:
                l += 1

        return []


# nums=[1,0,-1,0,-2,2]
# print (Solution().fourSum(nums))
# [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
# nums=[-3,-2,-1,0,0,1,2,3]
# print (Solution().fourSum(nums))
# print (len(Solution().fourSum(nums))) # 8
# [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

nums=[-3,-1,0,2,4,5]
print (Solution().fourSum(nums,2))
print (len(Solution().fourSum(nums,2)))
[[-3,-1,2,4]]


from contextlib import contextmanager
