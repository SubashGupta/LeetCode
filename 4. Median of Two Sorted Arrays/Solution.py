class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedlst=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>=nums2[j]:
                sortedlst.append(nums2[j])
                j+=1
            else:
                sortedlst.append(nums1[i])
                i+=1
        while i<len(nums1):
            sortedlst.append(nums1[i])
            i+=1
        while j<len(nums2):
            sortedlst.append(nums2[j])
            j+=1
        if len(sortedlst)%2==1:
            indexx = len(sortedlst)//2
            return sortedlst[indexx]
        else:
            return (sortedlst[len(sortedlst)//2]+sortedlst[len(sortedlst)//2-1])/2

        