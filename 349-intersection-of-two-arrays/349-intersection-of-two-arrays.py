class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = set()
        for i in nums1:
            if i in nums2:
                h.add(i)
            else:
                continue
        return list(h)