from Tokenizer import Tokenizer
from TypesData.number import  validatorNumber
from TypesData.Operation import validatorOperation, SYMBOL
from TypesData.Error import IsNotValue, ERROR, InvalidOperation

class lexer(): 
    def __init__(self, text:str) -> None:
        self.tokenizer:Tokenizer = Tokenizer(text)
        self.ResultValue = [] #Mas adelante nos ayudara mas aun
        self.message = ""
    def sendMessage(self, message: str):
        return f"Console: {message}"

    def lexerValue(self):
        for value in self.tokenizer.characters:
            if(self.tokenizer.isDigit(value) == True):
                self.ResultValue.append(validatorNumber(value))
            else:
                self.ResultValue.append(validatorOperation(value))
        return ""

    def lexerArithmetic(self):
        self.lexerValue()
        current = None
        prev = None
        next = None

        for seeker in range(len(self.tokenizer.characters)):
            for char in SYMBOL.symboltypes.values():
                if(self.tokenizer.characters[seeker] == char):
                    if len(self.tokenizer.characters) <= 2:
                        return print(InvalidOperation("Faltan Valores"))
                    current = self.tokenizer.characters[seeker]
                    prev = self.tokenizer.characters[seeker - 1]
                    next = self.tokenizer.characters[seeker + 1]
                    
                    prev = validatorNumber(prev) if self.tokenizer.isDigit(prev) == True else IsNotValue(prev)
                    next = validatorNumber(next) if self.tokenizer.isDigit(next) == True else IsNotValue(next)
                    break
        match current:
            case "+":
                operation = prev.showValue() + next.showValue()
            case "-":
                operation = prev.showValue() - next.showValue()
            case "*":
                operation = prev.showValue() * next.showValue()
            case "/":
                operation = prev.showValue() / next.showValue()
            case _:
                print(ERROR("SymbolError", "Simbolo No Identificado"))
        print(self.sendMessage(operation))
