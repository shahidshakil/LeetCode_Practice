class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        greatest = float('-inf')
        for i in sentences:
            count = 0
            for j in i.split():
                count+=1
            if count > greatest:
                greatest = count
        return greatest
            
            
        