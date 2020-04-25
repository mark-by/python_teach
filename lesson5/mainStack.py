from stack import Stack


def factorial(number):
    stack = Stack()
    while number > 1:
        stack.push(number)
        number -= 1
    result = 1
    while not stack.empty():
        result *= stack.pop()
    return result


def factorial_recursive(number):
    if number < 2:
        return 1
    return factorial_recursive(number - 1) * number


print(factorial(5))
print(factorial_recursive(5))
