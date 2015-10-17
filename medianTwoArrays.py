import math

__author__ = 'achau1'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return None
        size = len(nums1) + len(nums2)
        if not nums1:
            if len(nums2) == 1:
                return nums2[0]
            return self.fmsa(nums2[:size / 2], nums2[size / 2:], math.floor(size / 2), 0)
        if not nums2:
            if len(nums1) == 1:
                return nums1[0]
            return self.fmsa(nums1[:size / 2], nums1[size / 2:], math.floor(size / 2), 0)

        return self.fmsa(nums1, nums2, math.floor(size / 2), 0)

    def fmsa(self, nums1, nums2, target, taken):
        medIdxOne = int(math.floor(len(nums1) / 2))
        medValOne = nums1[int(medIdxOne)]
        medIdxTwo = int(math.floor(len(nums2) / 2))
        medValTwo = nums2[int(medIdxTwo)]

        if medValOne < medValTwo:
            if medIdxOne + taken + 1 > target:
                return self.fmsa(nums1[medIdxOne:], nums1[:medIdxOne], target, taken)
            elif medIdxOne + taken + 1 == target:
                return medValOne
            else:
                return self.fmsa(nums1[medIdxOne:], nums2, target, taken + medIdxOne +1 )
        else:
            if medIdxTwo + taken + 1 > target:
                return self.fmsa(nums2[medIdxTwo:], nums2[:medIdxTwo], target, taken)
            elif medIdxTwo + taken + 1 == target:
                return medValTwo
            else:
                return self.fmsa(nums2[medIdxTwo:], nums1, target, taken + medIdxTwo +1)


nums1 = [1, 1, 1, 1, 1]
nums2 = [5, 5, 5, 5]
x = Solution()
print(x.findMedianSortedArrays(nums1, nums2))
nums1 = [1, 1, 1, 1, 1, 100]
nums2 = [3, 5, 6, 7, 8, 9]
x = Solution()
print(x.findMedianSortedArrays(nums1, nums2))
nums1 = [1, 1, 1, 1, 1, 4]
nums2 = [3, 5, 6, 7, 8, 9]
x = Solution()
print(x.findMedianSortedArrays(nums1, nums2))
nums1 = [1, 1, 1, 9]
nums2 = [3, 5, 6, 7, 10, 11]
x = Solution()
print(x.findMedianSortedArrays(nums1, nums2))
nums1 = [1]
nums2 = [2, 3, 4]
x = Solution()
print(x.findMedianSortedArrays(nums1, nums2))
