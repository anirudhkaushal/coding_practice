# brute force solution - takes O(n^2) time
def pivotIndex(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = -1

        for i in range(len(nums)):
            left_nums = nums[:i]
            right_nums = nums[i+1:]

            sum_left = 0
            sum_right = 0

            for v in left_nums:
                sum_left += v

            for v in right_nums:
                sum_right += v

            if sum_left == sum_right:
                return i
            else:
                continue

        return ans


# optimal solution - takes O(n) time
def pivotIndex_optimal(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums) # O(n)
        
        leftSum = 0
        for i in range(len(nums)): # O(n)
            rightSum = total - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]

        return -1