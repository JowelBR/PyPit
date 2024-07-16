class Lexer:
    def __init__(self) -> None:
        self.operacion = 0

    def convertorNumeros(self, chr:str):
        for i in chr:
            if i in [",", "."]:
                return float(chr)
        if chr.isnumeric() or chr.__contains__("-") or chr.__contains__("+"):
            return int(chr)
        return chr

    def interpretador(self, prevValor: float, actualValor: str, SigValor: float) -> str:
        """
        Interpreta y realiza una operaciónes matemática sobre dos valores dados.
        
        Args:
            prevValor (float): El primer valor.
            actualValor (str): El operador (puede ser '+', '-', '*', '/').
            SigValor (float): El segundo valor.

        Returns:
            str: El resultado de la operación como una cadena.
        """
        if actualValor not in {"+", "-", "*", "/"}:
            raise ValueError("Operador no válido. No utiliza '+', '-', '*', o '/'.")

        match actualValor:
            case "+":
                return f"{prevValor + SigValor}"
            case "-":
                return f"{prevValor - SigValor}"
            case "*":
                return f"{prevValor * SigValor}"
            case "/":
                if(SigValor == 0): raise ZeroDivisionError("No puede dividir entre 0")
                return f"{prevValor / SigValor}"

    def ejecucion(self, previo, actual, siguiente):
            self.operacion = self.interpretador(self.convertorNumeros(previo), actual, self.convertorNumeros(siguiente))
            return self.operacion
    
    def mostrarResultado(self):
        return self.operacion