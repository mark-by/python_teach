from stackOnLesson import Stack

def factorial(number):
    stack = Stack()
    while number > 1:
        stack.push(number)
        number -= 1
    result = 1
    while not stack.empty():
        result *= stack.pop()
    return result

factorial(5)