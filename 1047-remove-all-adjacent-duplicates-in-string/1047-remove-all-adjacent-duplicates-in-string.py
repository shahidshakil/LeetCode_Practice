class Solution:
    def removeDuplicates(self, s: str) -> str:
        emptyString = []
        for c in s:
            if emptyString and emptyString[-1]==c:
                emptyString.pop()
            else:
                emptyString.append(c)
        return '' .join(emptyString)