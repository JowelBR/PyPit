from Jerarquia import Jerarquia as jr

while True:
    instruccion = input(">>>")
    jerarquia = jr(instruccion) 
    print(jerarquia.organizarEjecucion())