class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1]+stack[-2])

            elif op == "D":
                stack.append(2*stack[-1])

            elif op == "C":
                stack.pop()

            else:
                stack.append(int(op))

        return sum(stack)
