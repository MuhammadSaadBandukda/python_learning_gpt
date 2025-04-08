def calculator(*,number_01 , number_02):
    operators = ['+','-','*','/']
    print(operators)

    operation = input("Choose the operation:")

    # Match-case used to perform operation
    match(operation):
        case '+':
            return number_01 + number_02
        case '-':
            return number_01 - number_02
        case '*':
            return number_01 * number_02
        case '/':
            return number_01 / number_02
        case _:
            print("Invalid choice")
            return
        
def main():
    number_01 = int(input("Enter a Number:"))
    number_02 = int(input("Enter another Number:"))
    result = calculator(number_01=number_01,number_02=number_02)
    print(result)
main()
