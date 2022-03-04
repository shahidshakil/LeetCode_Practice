class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.remove(max(salary))
        salary.remove(min(salary))
        sum_ = sum(salary)
        length = len(salary)
        return sum_/length