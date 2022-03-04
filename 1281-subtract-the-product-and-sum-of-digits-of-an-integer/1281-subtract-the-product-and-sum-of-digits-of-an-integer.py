class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 0
        sum_ = 0
        product = 1
        while n>=1:
            digit = n%10
            sum_ += digit
            product = product*digit
            n = n//10
        
        difference  = product - sum_
        return difference
            
            
            
        