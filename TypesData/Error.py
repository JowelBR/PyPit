class ERROR:
    def __init__(self, name, message = "A FATAL ERROR"):
        self.name = name
        self.message = message

    def __repr__(self) -> str:
        return (f"{self.name}: {self.message}")

class InvalidOperation(ERROR):
    def __init__(self, symbol) -> None:
        self.name = InvalidOperation.__name__
        self.message = "La Operacion No Es Valida!"
        self.symbol = symbol 
        super().__init__(self.name, self.message)
    
    def __repr__(self) -> str:
        text = super().__repr__()
        return f"{text} Por: {self.symbol}"

class IsNotValue(ERROR):
    def __init__(self, expected):
        self.name = IsNotValue.__name__
        super().__init__(self.name)
        self.expected = expected
    
    def __repr__(self) -> str:
        text = super().__repr__()
        return f"{text}; {self.expected} No es el valor esperado..."

