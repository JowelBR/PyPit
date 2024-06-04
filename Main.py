from Lexer import lexer

while(True):
    intruccion = input(">>> ")
    if(intruccion == "exit"):
        break
    lex = lexer(intruccion)
    lex.lexerArithmetic()