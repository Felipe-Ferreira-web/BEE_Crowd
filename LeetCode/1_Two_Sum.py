# Problema: 1 - Two Sum
# Link: https://leetcode.com/problems/two-sum/description/


class Solution(object):

    def twoSum(self, nums, target):
        for indice1, valor1 in enumerate(nums):
            for indice2, valor2 in enumerate(nums):
                r = target - valor1
                if valor2 == r and indice1 != indice2:
                    return [indice1, indice2]
