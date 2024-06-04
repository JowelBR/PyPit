from TypesData.number import validatorNumber

class Tokenizer:
    def __init__(self, text:str):
        self.text = text
        self.characters = []
        self.withoutSpace = []
        self.separate()
    
    def separate(self):
        char = ""
        for character in self.text:
            if character == "+" or character == "-" or character == "*" or character == "/" or character == " ":
                self.characters.append(char)
                self.characters.append(character)
                char = ""
                continue
            char += character
        if(char):
            self.characters.append(char)
        self.withoutSpace = self.characters.copy()
        self.characters = list(filter(lambda x: x != " " and x != "", self.characters))

        
    
    def findCharacter(self, character):
        for index, obj in enumerate(self.characters):
            if obj == character:
                return index
    
    def isDigit(self, char):
        try:
            char = validatorNumber(char)
            if bool(char):
                return True
        except ValueError: return False

