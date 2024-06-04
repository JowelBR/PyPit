from TypesData.Error import InvalidOperation

class SYMBOL:
    symboltypes = {'SUM':'+', "SUB":'-', 'MULT':"*", "DIV":"/", "LPAREN":"(", "RPAREN":")"}
    def __init__(self, symbol) -> None:
        self.symbol = symbol

    def __repr__(self) -> str:
        for key, value in self.symboltypes.items():
            if(value == self.symbol):
                return f"{key}:{value}"

def validatorOperation(symbol:str):
    match symbol:
        case "+":
            return SYMBOL("+")
        case "-":
            return SYMBOL("-")
        case "*":
            return SYMBOL("*")
        case "/":
            return SYMBOL("/")
        case "(":
            return SYMBOL("(")
        case ")":
            return SYMBOL(")")
    return InvalidOperation(symbol)
