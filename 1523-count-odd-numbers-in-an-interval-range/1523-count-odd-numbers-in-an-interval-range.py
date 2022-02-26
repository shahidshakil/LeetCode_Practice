class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low%2 == 0:
            lowerbound = low+1
        else:
            lowerbound = low
        if high%2 == 0:
            upperbound = high-1
        else:
            upperbound = high
        print(upperbound,lowerbound)
        number = ((upperbound - lowerbound) //2) +1
        return number