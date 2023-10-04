from typing import List
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    if (len(nums)<=1):
        print("length error")
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if ((nums[i]+nums[j])==target):
                print([i,j])
                return [i,j]
    return