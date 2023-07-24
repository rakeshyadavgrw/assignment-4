#***************Q1**************#
class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        def find(arr, val):
            left, right = 0, len(arr) - 1
            while left < right:
                mid = (left + right) >> 1
                if arr[mid] >= val:
                    right = mid
                else:
                    left = mid + 1
            return arr[left] == val

        res = []
        for num in arr1:
            if find(arr2, num) and find(arr3, num):
                res.append(num)
        return res
    #******************Q2*********************#
    class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[]
        a=[]
        a=set(nums1) - set(nums2)
        b=[]
        b=set(nums2) - set(nums1)
        res.append(a)
        res.append(b)
        return res
    #******************Q3*********************#
    class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n=len(matrix),len(matrix[0])
        ans = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][i]=matrix[i][j]
        
        return ans
    #******************Q4*********************#
    class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_ = 0
        for i in range(0,len(nums),2):
            sum_ += nums[i]
        return sum_

# Time : 356 ms
# Memory : 16.7 M
 #******************Q5*********************#
 def arrangeCoins(self, n: int) -> int:
    return int((-1 + (1 + 8*n) ** 0.5) // 2)
#******************Q6*********************#
class Solution:
    
    def generate_sorted_squares(self, nums):
        
        # Start by doing our binary search to find where
        # to place the pointers.
        left = 0
        right = len(nums)
        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[mid] > 0:
                right = mid
            else:
                left = mid
        
        # And now the main generator loop. The condition is the negation
        # of the StopIteration condition for the iterator approach.
        while left >= 0 or right < len(nums):
            if left < 0:
                right += 1
                yield nums[right - 1] ** 2
            elif right >= len(nums):
                left -= 1
                yield nums[left + 1] ** 2
            else:
                left_square = nums[left] ** 2
                right_square = nums[right] ** 2
                if left_square < right_square:
                    left -= 1
                    yield left_square
                else:
                    right += 1
                    yield right_square
        
    
    def sortedSquares(self, A: List[int]) -> List[int]:
        return list(self.generate_sorted_squares(A))
    #******************Q7*********************#
    class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row = m
        min_col = n
        for i in range(len(ops)):
            min_row=min(min_row, ops[i][0])
            min_col=min(min_col, ops[i][1])
        return min_row*min_col
    #******************Q8*********************#
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res
        
    