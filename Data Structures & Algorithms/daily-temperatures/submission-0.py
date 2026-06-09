class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []
        for i in range(n):
            count = 0
            j = i
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                count += 1
            if j == n:
                res.append(0)
                continue
            res.append(count)
        return res