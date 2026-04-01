class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = 0
        record = []
        for i in range(len(operations)):
            match operations[i]:
                case "C":
                    result -= record.pop()
                    continue
                case "+":
                    value = record[-1] + record[-2]
                case "D":
                    value = record[-1] * 2
                case _:
                    value = int(operations[i])
            result += value
            record.append(value)

        return result