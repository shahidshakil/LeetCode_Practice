class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverseNum=0
        sign=1
        if(x<1):
            sign=-1
            x=abs(x)
        while x>=1:
            digit=x%10
            reverseNum=reverseNum*10+digit
            x=x//10
        if reverseNum<=2**31 and x>=(-2**31)-1:
            return(reverseNum*sign)
             
        
        else:
            return 0
            

