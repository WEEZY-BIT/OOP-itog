import logging
from calculator.complex_number import ComplexNumber
from calculator.operations import AddOperation, MultiplyOperation, DivideOperation
from calculator.calculator import Calculator

# Настройка логирования
logging.basicConfig(filename='logs/calculator.log', level=logging.INFO)

def main():
    # Инициализация комплексных чисел
    num1 = ComplexNumber(3, 2)
    num2 = ComplexNumber(1, 7)

    # Калькулятор для сложения
    calculator = Calculator(AddOperation())
    result = calculator.calculate(num1, num2)
    print(f"Result of addition: {result}")

    # Калькулятор для умножения
    calculator.set_strategy(MultiplyOperation())
    result = calculator.calculate(num1, num2)
    print(f"Result of multiplication: {result}")

    # Калькулятор для деления
    calculator.set_strategy(DivideOperation())
    result = calculator.calculate(num1, num2)
    print(f"Result of division: {result}")

if __name__ == "__main__":
    main()