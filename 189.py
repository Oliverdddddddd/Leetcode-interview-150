class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        j = k % len(nums)
        def rev(i:int,j:int):
            start = i 
            end = j
            while (start < end):
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp 
                start += 1
                end-=1
        rev(0,j-1)
        rev(j,len(nums)-1)
