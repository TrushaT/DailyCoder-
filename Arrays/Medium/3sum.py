'''
Date - 14/01/2020

Link to the problem : https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Related Topic - Two pointers 

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3 :
            return []
        nums.sort()
        ans = []
        for a in range(len(nums)-2):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            b = a + 1
            c = len(nums) -1 
            while(b < c):
                if nums[a]+nums[b]+nums[c] > 0 :
                    c -=1 
                elif nums[a]+nums[b]+nums[c]<0:
                    b += 1
                else :
                    ans.append([nums[a],nums[b],nums[c]])
                    b += 1
                    while nums[b] == nums[b-1] and b < c:
                        b += 1
        return ans
                
            