from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]

        def helo(path,remaining):
            if not remaining:
                result.append(path)
                return

            for i in range(len(remaining)):
                helo(path+[remaining[i]],remaining[:i]+remaining[i+1:])
        helo([],nums)
        return result
