#coding: utf8


'''
两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_set = set(nums)
        for i,num_i in enumerate(nums):
            r = target - num_i
            if r == num_i:
                if r in nums[i+1:]:
                    return [nums.index(r, i+1), i]

            elif r in nums_set:
                return [nums.index(r, i+1),i]
        return []


print (Solution().twoSum([2,7,11,15], 9))
print (Solution().twoSum([2,7,2,15], 4))

# ------------------------------------------------------


class Solution(object):
    def twoSum(self, nums, target):
        # res = []
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            s = - target + nums[l] + nums[r]
            if s == 0:
                return [nums[l], nums[r]]
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

        return []

print (Solution().twoSum([2,7,11,15], 9))
print (Solution().twoSum([2,7,2,15], 4))
print (Solution().twoSum([3,2,4], 6))