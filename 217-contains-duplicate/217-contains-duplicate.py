class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_dic = {}
        for i in nums:
            if i in count_dic:
                count_dic[i]+=1
            else:
                count_dic[i] = 1
        for i in count_dic.values():
            if i > 1:
                return True
        return False