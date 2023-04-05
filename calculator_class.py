class Calculator:
    #constructing the atributs
    def __init__(self, num1=0, num2=1):
        self.num1 = 0
        self.num2 = 1
        if num1 != "":
            self.num1 = int(num1)
        if num2 != "":
            self.num2 = int(num2)

    # definig the methods
    def add(self):
        print(f"{self.num1} + {self.num2} = {self.num1+self.num2}")
    def sub(self):
        print(f"{self.num1} - {self.num2} = {self.num1-self.num2}")
    def mult(self):
        print(f"{self.num1} * {self.num2} = {self.num1*self.num2}")
    def div(self):
        if self.num2==0:
            print(f"{self.num1} / {self.num2} = Division by 0")
        else:
            print(f"{self.num1} / {self.num2} = {self.num1/self.num2}")

class Power(Calculator):
    def pow(self):
        if self.num2==0:
            print(f"{self.num1} ^ {self.num2} = 1")
        else:
            print(f"{self.num1} ^ {self.num2} = {self.num1**self.num2}")

n1 = input("First number: ")
n2 = input("Second number: ")
my_calculator = Calculator(n1,n2)
my_calculator.add()
my_calculator.sub()
my_calculator.mult()
my_calculator.div()
my_power = Power(5,10).pow() # poti crea un obiect si apela una din metodele lui in aceiasi linie
