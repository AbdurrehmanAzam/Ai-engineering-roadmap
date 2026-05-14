class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real}i + {self.imag}j"

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)

    def __sub__(self, other):
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        return Complex(new_real, new_imag)


num1 = Complex(1, 3)
print(num1)

num2 = Complex(4, 6)
print(num2)

num3 = num1 + num2
print(num3)

num4 = num2 - num1
print(num4)
