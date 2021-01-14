'''
Date - 12/01/2020

Link to the problem : https://leetcode.com/problems/container-with-most-water/ 

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Related Topic - Two pointers 

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        start = 0 
        end = len(height) - 1 
        while (start != end):
            vol = (end-start)*min(height[start],height[end])
            if vol > max_water :
                max_water = vol
            if height[start] > height[end]:
                end -= 1
            else :
                start += 1
        return max_water


        

        
                
            
            
            

