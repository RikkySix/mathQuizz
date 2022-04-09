from random import randint
operators = ["+", "-", "*"]

mark = 0

print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")

while True:
    try:
        answer = int(input())
        if answer == 1:
            for i in range(5):
                x = randint(2, 9)
                y = randint(2, 9)
                op = operators[randint(0, 2)]
                print(f"{x} {op} {y}")
                result = None
                if op == "+":
                    result = int(x) + int(y)
                elif op == "-":
                    result = int(x) - int(y)
                elif op == "*":
                    result = int(x) * int(y)

                while True:
                    try:
                        u_result = int(input())
                        break
                    except ValueError:
                        print("Incorrect format.")

                if u_result == result:
                    print("Right!")
                    mark += 1
                else:
                    print("Wrong!")
            message = "in level 1 (simple operations with numbers 2-9)"
            break
        elif answer == 2:
            for i in range(5):
                x = randint(11, 29)
                print(x)
                result = x ** 2
                while True:
                    try:
                        u_result = int(input())
                        break
                    except ValueError:
                        print("Incorrect format.")
                if u_result == result:
                    print("Right!")
                    mark += 1
                else:
                    print("Wrong!")
            message = "in level 2 (integral squares 11-29)"
            break
        else:
            raise ValueError
    except ValueError:
        print("Incorrect format.")







print(f"Your mark is {mark}/5. Would you like to save your result to the file? Enter yes or no.")

answer = input().lower()
if answer in ["Yes", "YES", "yes", "y", "Y"]:
    print("What is your name?")
    name = input()

    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}: {mark}/5 {message} ")
    file.close()
    print('The results are saved in "results.txt".')

elif answer == "no":
    pass


