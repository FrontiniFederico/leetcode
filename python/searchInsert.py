class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            done = False
            low = 0 
            high = len(nums-1)

            while not done:
                middle = (low + high)//2
                if nums[middle] < target:
                    low = middle + 1
                else:
                    high = middle - 1

                if low > high: 
                    done = True
            return low 
               
