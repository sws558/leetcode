from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        if m==0:
            nums1[0]=nums2[0]
        nums1_pointer=m-1
        nums2_pointer=n-1
        pointer=m+n-1
        while nums1_pointer>=0 and nums2_pointer>=0:
            if nums1[nums1_pointer]>nums2[nums2_pointer]:
                nums1[pointer]=nums1[nums1_pointer]
                nums1_pointer=nums1_pointer-1
            else:
                nums1[pointer]=nums2[nums2_pointer]
                nums2_pointer=nums2_pointer-1

            pointer=pointer-1
        if nums1[nums1_pointer]==-1 and nums2[nums2_pointer]==0:
            nums1[0]=nums2[0]
if __name__ == "__main__":
    nums1=[1,2,3,0,0,0]
    nums2=[2,5,6]
    solution=Solution()
    solution.merge(nums1,3,nums2,3)
    print(nums1)


