class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1

        #always try ot locate the sorted side and find the target from the sorted side
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid


            elif nums[mid] >nums[r]: #left side is sorted
                if target <= nums[mid-1] and target >= nums[l]:
                    r = mid -1
                else: 
                    l = mid + 1


            else: # right side is sorted
                #if target <= nums[r] and target >= nums[mid + 1]:
                if target <= nums[r] and target >= nums[mid]:
                    l = mid + 1
                else: 
                    r = mid - 1
        return -1