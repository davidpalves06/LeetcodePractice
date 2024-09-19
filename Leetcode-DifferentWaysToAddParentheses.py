class Solution:
    def diffWaysToCompute(self, expression: str):
        res = [];
        for i in range(len(expression)):
            char = expression[i];
            if (char == '*' or char == '-' or char == '+'):
                leftExpression = expression[0:i];
                rightExpression = expression[i+1:];
                leftResults = self.diffWaysToCompute(leftExpression);
                rightResults = self.diffWaysToCompute(rightExpression);
                for leftResult in leftResults:
                    for rightResult in rightResults:
                        if (char == '*'):
                            res.append(int(leftResult) * int(rightResult));
                        if (char == '-'):
                            res.append(int(leftResult) - int(rightResult));
                        if (char == '+'):
                            res.append(int(leftResult) + int(rightResult))
        if (len(res) == 0):
            res.append(int(expression))
        return res
    