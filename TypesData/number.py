class number:
    def __init__(self, value) -> None:
        self.value = value
        self.type = "Number"
    def __repr__(self) -> str:
        return f"{self.type}:{self.value}"
    
    def showValue(self):
        return self.value
    
    def showType(self):
        return self.type

class numberVoid(number):
    def __init__(self):
        self.type = "NumberVoid"
        self.value = None

class INT(number):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.type = "INT"
        self.value = int(self.value)
    
class FLOAT(number):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.type = "FLOAT"
        self.value = float(self.value)
    

def validatorNumber(num: int | float):
    for i in str(num):
        if(i == "."):
            return FLOAT(num)
    return INT(num)
