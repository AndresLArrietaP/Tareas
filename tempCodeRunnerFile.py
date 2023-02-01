import re

#Definimos la funcion caracter 
def caracter(character):
    global simbolo
    simbolo=""
    global Fin
    Fin=""
    iden="[a-zA-Z_][a-zA-Z0-9_]"
    reser="(int|float|double|char|string|byte|void)"
    prin="main"
    signos="(\(|\)|\{|\}|;|,)"
    digito="[0-9]"
    operador="(+|-|*|/)"
    
    #comparamos si es digito o operador
    if(re.match(reser,character)):
        simbolo=" Tipo "
        return 0
    else:
        if(re.match(prin,character)):
            simbolo="Main"
            return 2
        else:
            if(re.match("\(",character)):
                simbolo="ParIzq"
                return 3
            else:
                if(re.match("\)",character)):
                    simbolo="ParDer"
                    return 4
                else:
                    if(re.match("\{",character)):
                        simbolo="LlaIzq"
                        return 5
                    else:
                        if(re.match("\}",character)):
                            simbolo="LlaDer"
                            return 6
                        else:
                            if(re.match("\,",character)):
                                simbolo="Coma"
                                return 7
                            else:
                                if(re.match("\$",character)):
                                    simbolo="FinExp"
                                    return 8
                                else:
                                    if(re.match(iden,character)):
                                        simbolo="Identificador"
                                        return 1
                                    else:
                                        if(character==Fin):
                                            return 9
                                    #si no es ni un digito ni un operador entonces es un caracter no validp
                                    print("Error el ",character,"no es valido")
                                    exit()

#definimos al la funcion  encabezado
def encabezado():
    print("""|  Edo. Actual |Caracter |  Simbolo  |Edo. Siguiente |""")
    body()

#definimos la funcion contenido donde guarda cada valor despues de encontrarlo en un ciclo
def contenido(estadosig,character,simbolo,estado):
    print("|     ",estadosig,"      |  ",character,"    |",simbolo," |     ",estado,"       |")
    body()

#solo muestra la linea que se repetira cada vez que la mandemos a llamar
def body():
    print("+--------------+---------+-----------+---------------+")

#MAIN
#Este es la tabla de transiciones del automata AFD creado
tabla=[[1,"E",7,"E","E","E","E","E","E","E"]
      ,["E",2,"E","E","E","E","E","E","E","E"]
      ,["E","E","E",3,"E","E","E","E","E","E"]
      ,[12,"E","E","E",4,"E","E","E","E","E"]
      ,["E","E","E","E","E",5,"E","E","E","E"]
      ,["E","E","E","E","E","E",6,"E","E","E"]
      ,[1,"E",7,"E","E","E","E","E","E","E"]
      ,["E","E","E",8,"E","E","E","E","E","E"]
      ,["E","E","E","E",9,"E","E","E","E","E"]
      ,["E","E","E","E","E",10,"E","E","E","E"]
      ,["E","E","E","E","E","E",11,"E","E","E"]
      ,["E","E","E","E","E","E","E","E",15,"E"]
      ,["E",13,"E","E",4,"E","E","E","E","E"]
      ,["E","E","E","E",4,"E","E",14,"E","E"]
      ,[12,"E","E","E","E","E","E","E","E","E"]
      ,["E","E","E","E","E","E","E","E","E","A"]]
estado = 0

print ("""+-------------------------------------+
|    Ingrese una cadena a evaluar:    |
+-------------------------------------+""")
cadena = input()
exp=cadena+" $"
entrada=exp.split(sep=" ")
body()
encabezado()

#ciclo para recorrer la cadena
for  character in entrada:
    estadosig=estado
    
    #llamamos al metodo para saber si es un caracter valido y el valor retornado se guarda en charcaracter
    charcaracter= caracter(character)
    
    #guardamos en estado el valor obtenido en la tabla segun las cordenadas que recibio anteriormente
    estado=tabla[estado][charcaracter]
    
    #Si el valor obtenido es una E imprimimos cadena no valida
    if (estado=="E"):
        print("|     ",estadosig,"      |  ",character,"    |",simbolo," |     ",estado,"       |")
        body()
        print("""|              Cadena No Valida :(                   |
+----------------------------------------------------+""")
        exit()
    contenido(estadosig,character,simbolo,estado)

#al concluir si el estado no es 3 que es el de aceptacion imprimimos cadena no valida    
if(estado!=15):
        print("""|              Cadena No Valida :(                   |
+----------------------------------------------------+""")

#si el estado es 3 es una cadena de aceptacion
if(estado==15):
    print("|     ",estado,"      |         |    FND    |               |")
    body()
    print("""|                Cadena Valida :)                    |
+----------------------------------------------------+""")