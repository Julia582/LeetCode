class Solution(object):
    def compareVersion(self, version1, version2):
        i,j=0,0
        n,m=len(version1),len(version2)
        while i<n or j<m :
            nums1=nums2=0
            while i<n and version1[i]!='.':
                nums1=nums1*10+int(version1[i])
                i+=1
            while j<m and version2[j]!='.':
                nums2=nums2*10+int(version2[j])
                j+=1
            if nums1>nums2:
                return 1
            if nums1<nums2:
                return -1
            i+=1
            j+=1
        return 0

            
       