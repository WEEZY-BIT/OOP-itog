from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class AddOperation(OperationStrategy):
    def execute(self, a, b):
        result = ComplexNumber(a.real + b.real, a.imag + b.imag)
        logger.info(f"Adding {a} + {b} = {result}")
        return result

class MultiplyOperation(OperationStrategy):
    def execute(self, a, b):
        real = a.real * b.real - a.imag * b.imag
        imag = a.imag * b.real + a.real * b.imag
        result = ComplexNumber(real, imag)
        logger.info(f"Multiplying {a} * {b} = {result}")
        return result

class DivideOperation(OperationStrategy):
    def execute(self, a, b):
        denominator = b.real ** 2 + b.imag ** 2
        if denominator == 0:
            raise ValueError("Cannot divide by zero.")
        real = (a.real * b.real + a.imag * b.imag) / denominator
        imag = (a.imag * b.real - a.real * b.imag) / denominator
        result = ComplexNumber(real, imag)
        logger.info(f"Dividing {a} / {b} = {result}")
        return result