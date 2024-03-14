from typing import  List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:]=[0 if x==val else x for x in nums]
        nums.sort(reverse=True)
        i=0
        for num in nums:
            if num !=0:
                i=i+1
        return i
if __name__ == "__main__":
    solution=Solution()
    nums=[0,1,2,2,3,0,4,2]
    val=2
    solution.removeElement(nums,val)
    print(nums)
