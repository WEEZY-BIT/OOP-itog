class Calculator:
    def __init__(self, strategy: OperationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: OperationStrategy):
        self._strategy = strategy

    def calculate(self, a, b):
        return self._strategy.execute(a, b)