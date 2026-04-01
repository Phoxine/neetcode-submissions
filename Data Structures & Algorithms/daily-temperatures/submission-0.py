class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []        
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):

            # find all element in stack which is smaller than current temperature
            while stack and temperatures[i] > stack[-1][1]:
                index, temperature = stack.pop()
                result[index] = i - index
            stack.append((i, temperatures[i]))

        return result