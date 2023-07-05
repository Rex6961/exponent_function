import time

def funcTime(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        elapsed = end - start
        return elapsed
    return wrapper

#This is Iteration exponent function
@funcTime
def exponentByIteration(number, n):
    result = 0
    for i in range(0, n):
        result *= number
    return result

#This is iteration exponent function how recursive function
@funcTime
def exponentWithPowerRule(a, n):
    opStack = []
    while n > 1:
        if n % 2 == 0:
            opStack.append('square')
            n = n // 2
        elif n % 2 == 1:
            n -= 1
            opStack.append('multiply')

    result = a
    while opStack:
        op = opStack.pop()

        if op == 'multiply':
            result *= a
        elif op == 'square':
            result *= result

    return result

#This is recursive exponent function
@funcTime
def exponentByRecursion(number, n):
    if n == 1:
        return number
    if n % 2 == 0:
        result = exponentByRecursion(number, n // 2)
        return result * result
    elif n % 2 == 1:
        result = exponentByRecursion(number, n // 2)
        return result * result * number



if __name__ == '__main__':
    print(exponentByIteration(3, 1000))
    print(exponentWithPowerRule(3, 1000))
    print(exponentByRecursion(3, 1000))
