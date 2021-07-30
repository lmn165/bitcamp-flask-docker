from grade import Grade;
# Calculator 클래스는 object 클래스를 상속한다.


class Calculator(object):

    # Domain은 결국 속성 값들을 담는 정형화 된 객체이기 때문에 아래와 같이 간략하게 생략하여 사용한다.
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def remain(self):
        return self.num1 % self.num2

    @staticmethod
    def main():
        while 1:
            menu = input('0-Exit 1: + 2: - 3: * 4: / 5: % 6: 학점\n')
            if menu == '0':
                return
            elif menu == '1':
                num1 = int(input('first number: '))
                num2 = int(input('second number: '))
                calc = Calculator(num1, num2)
                print(f'{calc.num1} + {calc.num2} = {calc.add()}')
                print('*' * 100)
                continue
            elif menu == '2':
                num1 = int(input('first number: '))
                num2 = int(input('second number: '))
                calc = Calculator(num1, num2)
                print(f'{calc.num1} - {calc.num2} = {calc.subtract()}')
                print('*' * 100)
                continue
            elif menu == '3':
                num1 = int(input('first number: '))
                num2 = int(input('second number: '))
                calc = Calculator(num1, num2)
                print(f'{calc.num1} * {calc.num2} = {calc.multiple()}')
                print('*' * 100)
                continue
            elif menu == '4':
                num1 = int(input('first number: '))
                num2 = int(input('second number: '))
                calc = Calculator(num1, num2)
                print(f'{calc.num1} / {calc.num2} = {calc.divide()}')
                print('*' * 100)
                continue
            elif menu == '5':
                num1 = int(input('first number: '))
                num2 = int(input('second number: '))
                calc = Calculator(num1, num2)
                print(f'{calc.num1} % {calc.num2} = {calc.remain()}')
                print('*' * 100)
                continue
            elif menu == '6':
                Grade.avercontroll(self=Grade)
                continue
            else:
                print('Wrong Selected Number')


Calculator.main()
