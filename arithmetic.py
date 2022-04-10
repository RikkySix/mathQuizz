import random
import string


class ArithmeticExamApplication:
    def __init__(self):
        self.level = None
        self.level_text = None
        self.operand1 = None
        self.operand2 = None
        self.operator = None
        self.result = None
        self.correct_answers = 0

    def addition(self):
        return self.operand1 + self.operand2

    def subtraction(self):
        return self.operand1 - self.operand2

    def multiplication(self):
        return self.operand1 * self.operand2

    def calculate(self):
        if self.operator == "+":
            result = self.addition()
        elif self.operator == "-":
            result = self.subtraction()
        elif self.operator == "*":
            result = self.multiplication()
        else:
            raise ValueError

        return result

    def generate_task_level_1(self):
        self.operand1 = random.choice(range(2, 10))
        self.operand2 = random.choice(range(2, 10))
        self.operator = random.choice(['+', '-', '*'])
        self.result = self.calculate()

        return f"{self.operand1} {self.operator} {self.operand2}"

    def generate_task_level_2(self):
        self.operand1 = random.choice(range(11, 30))
        self.operand2 = self.operand1
        self.operator = '*'
        self.result = self.calculate()

        return f"{self.operand1}"

    def ask_for_level(self):
        while True:
            print("Which level do you want? Enter a number:")
            print("1 - simple operations with numbers 2-9")
            print("2 - integral squares of 11-29")
            self.level = int(input())

            if self.level in [1, 2]:
                break
            else:
                print("Incorrect format.")

    def ask_for_storing(self):
        print("Would you like to save your result to the file? Enter yes or no.")
        store = input()
        if store in ['yes', 'YES', 'y', 'Yes']:
            name = input("What is your name?\n")
            txt = f"{name}: {self.correct_answers}/5 in level {self.level} ({self.level_text}).\n"
            with open('results.txt', 'a') as f:
                f.write(txt)
                f.close()

            print("The results are saved in \"results.txt\".")

    def play(self):
        for i in range(5):
            if self.level == 1:
                self.level_text = "simple operations with numbers 2-9"
                task = self.generate_task_level_1()
            elif self.level == 2:
                self.level_text = "integral squares of 11-29"
                task = self.generate_task_level_2()
            else:
                raise ValueError

            print(task)

            while True:
                try:
                    answer = int(input())

                except ValueError:
                    print("Incorrect Format")
                    continue

                else:
                    if int(answer) == self.result:
                        print("Right!")
                        self.correct_answers += 1
                    else:
                        print("Wrong!")

                    break

        print(f"Your mark is {self.correct_answers}/5")

    def main(self):
        self.ask_for_level()
        self.play()
        self.ask_for_storing()


if __name__ == '__main__':
    ArithmeticExamApplication().main()
