class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        op1=[]
        d={}
        for i in range(len(nums2)):
            d[nums2[i]] = i
        for j in nums1:
            indexStart = d[j] + 1
            maxi=-1
            while indexStart<len(nums2):
                if nums2[indexStart]>j:
                    maxi = nums2[indexStart]
                    break
                indexStart+=1
            op1.append(maxi)
        return op1