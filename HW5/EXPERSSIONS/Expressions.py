class Expression:
    OPERATORS = ['*', '/', '+', '-']
    OPERATORS_PRECEDENCE = {
        '*': 2, '/': 2, '+': 1, '-': 1
    }

    def __init__(self, expression):
        self.expression = expression

    @staticmethod
    def calculate(operand_1, operand_2, operator):
        if operator == '+':
            return operand_1 + operand_2
        elif operator == '-':
            return operand_1 - operand_2
        elif operator == '*':
            return operand_1 * operand_2
        elif operator == '/':
            return operand_1 / operand_2

    @staticmethod
    def is_operator(char):
        return char in Expression.OPERATORS

    @staticmethod
    def is_higher_precedence(operator1, operator2):
        return Expression.OPERATORS_PRECEDENCE[operator1] > Expression.OPERATORS_PRECEDENCE[operator2]

    @staticmethod
    def get_variable_value(variable_dict, variable_name):
        if variable_name in variable_dict:
            return variable_dict[variable_name]
        else:
            raise KeyError(f"Variable '{variable_name}' not found in the provided values.")
       

class ExpressionFactory:
    @staticmethod
    def create_expression(expression, expression_type):
        if expression_type == "infix":
            return InfixExpression(expression)
        elif expression_type == "postfix":
            return PostfixExpression(expression)
        elif expression_type == "prefix":
            return PrefixExpression(expression)
        else:
            raise ValueError("Invalid expression type. Supported types: infix, postfix, prefix.")
  

class InfixExpression(Expression):
    def __init__(self, expression):
        super().__init__(expression)

    def evaluate(self, variable_values):
        postfix_expression = PostfixExpression(self.to_postfix())
        return postfix_expression.evaluate(variable_values)

    def to_postfix(self):
        postfix_result = []
        operator_stack = []

        for char in self.expression:
            if not self.is_operator(char) and char not in ['(', ')']:
                postfix_result.append(char)
        
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    postfix_result.append(operator_stack.pop(-1))
        
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop(-1)
        
            elif self.is_operator(char):
                while (operator_stack and operator_stack[-1] != '(' and
                    not self.is_higher_precedence(char, operator_stack[-1])):
                    postfix_result.append(operator_stack.pop())

                operator_stack.append(char)
        
        while operator_stack:
            postfix_result.append(operator_stack.pop())
        
        return ''.join(postfix_result)
   

class PostfixExpression(Expression):
    def __init__(self, expression):
        super().__init__(expression)

    def evaluate(self, variable_values):
        operand_stack = []

        for char in self.expression:
            if not self.is_operator(char):
                operand_stack.append(self.get_variable_value(variable_values, char))

            else:
                if len(operand_stack) >= 2:
                    operand_2 = operand_stack.pop()
                    operand_1 = operand_stack.pop()
                    result = self.calculate(operand_1, operand_2, char)
                    operand_stack.append(result)
                else:
                    raise ValueError("Invalid postfix expression: insufficient operands.")
        
        if len(operand_stack) != 1:
            raise ValueError("Invalid postfix expression: too many operands.")
        return operand_stack[0]



class PrefixExpression(Expression):
    def __init__(self, expression):
        super().__init__(expression)

    def evaluate(self, variable_values):
        operand_stack = []
        reversed_expression = self.expression[::-1]

        for char in reversed_expression:
            if not self.is_operator(char):
                operand_stack.append(self.get_variable_value(variable_values, char))
            else:
                if len(operand_stack) >= 2:
                    operand_1 = operand_stack.pop()
                    operand_2 = operand_stack.pop()
                    result = self.calculate(operand_1, operand_2, char)
                    operand_stack.append(result)
                else:
                    raise ValueError("Invalid prefix expression: insufficient operands.")
        
        if len(operand_stack) != 1:
            raise ValueError("Invalid prefix expression: too many operands.")
        return operand_stack[0]
    
    def to_postfix(self):
        postfix_expression = []
        reversed_expression = self.expression[::-1]
        for char in reversed_expression:
            if not self.is_operator(char):
                postfix_expression.append(char)
            elif self.is_operator(char):
                operand_1 = postfix_expression.pop(-1)
                operand_2 = postfix_expression.pop(-1)
                temp_operand = f"{operand_1}{operand_2}{char}"
                postfix_expression.append(temp_operand)
        
        return ''.join(postfix_expression)




expression = 'c*(a+b)'
variable_values = {
    "a": 1,
    "b": 2,
    "c": 3
}


infix_expression = ExpressionFactory.create_expression(expression=expression, expression_type='infix')
result = infix_expression.evaluate(variable_values)
print("Result:", result)
