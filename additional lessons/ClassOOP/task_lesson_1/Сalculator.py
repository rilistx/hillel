class Calculator:
    def __init__(self, num_1, operator, num_2):
        self.num_1 = num_1
        self.operator = operator
        self.num_2 = num_2

    def result(self):
        if self.operator == "+":
            print(self.num_1 + self.num_2)
        elif self.operator == "-":
            print(self.num_1 - self.num_2)
        elif self.operator == "/":
            print(self.num_1 / self.num_2)
        elif self.operator == "*":
            print(self.num_1 * self.num_2)
        else:
            print("CalculationError!")


calculator = Calculator(45, "*", -0.3)
calculator.result()
