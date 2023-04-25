def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


Dict = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}


def calculator():

    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))

    for x in Dict:
        print(x)
    operation = input("pick a operation from above symbols: ")

    b = Dict[operation]
    answer1 = b(num1, num2)
    print(f"{num1} {operation} {num2} = {answer1}")

    condition = input(f"type 'y' to continue with {answer1}, or type 'n' to start new calculation: ")
    if condition == "y":
        while condition == "y":
            operation = input("pick a operation: ")
            num3 = float(input("write another number: "))
            b = Dict[operation]
            answer2 = b(answer1, num3)
            print(f"{answer1} {operation} {num3} = {answer2}")

            condition = input(f"type 'y' to continue with {answer2}, or type 'n' start new calculation: ")
            if condition == "y":
                condition = "y"
    else:
        calculator()
calculator()
