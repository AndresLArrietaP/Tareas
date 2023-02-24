import re
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.lookahead = self.tokens[self.index]

    def match(self, expected_token):
        if self.lookahead == expected_token:
            self.index += 1
            if self.index < len(self.tokens):
                self.lookahead = self.tokens[self.index]
            else:
                self.lookahead = None
        else:
            raise ValueError("Error de sintaxis")

    def S(self):
        self.match("struct")
        self.A()
        self.match("{")
        self.B()
        self.match("}")
        self.C()
        self.match(";")

    def A(self):
        self.iden="[a-zA-Z_][a-zA-Z0-9_]"
        if re.match(self.iden,self.lookahead):
            #re.match(self.iden,self)
            self.match(self.lookahead)
        else:
            pass # A -> ε

    def B(self):
        self.iden="[a-zA-Z_][a-zA-Z0-9_]"
        if self.lookahead in ["int", "float", "double", "char", "bool", "string"]:
            self.D()
            while re.match(self.iden,self.lookahead):
                self.D()
        else:
            pass # B -> ε

    def D(self):
        self.E()
        self.match(self.lookahead)
        self.match(";")
        self.W()
    
    def W(self):
        self.iden="[a-zA-Z_][a-zA-Z0-9_]"
        if self.lookahead in ["int", "float", "double", "char", "bool", "string"]:
            self.D()
            while re.match(self.iden,self.lookahead):
                self.D()
        else:
            pass # B -> ε

    def E(self):
        if self.lookahead in ["int", "float", "double", "char", "bool", "string"]:
            self.match(self.lookahead)
        else:
            raise ValueError("Error de sintaxis")

    def C(self):
        self.iden="[a-zA-Z_][a-zA-Z0-9_]"
        if re.match(self.iden,self.lookahead):
            self.F()
        else:
            pass # C -> ε

    def F(self):
        self.match(self.lookahead)
        self.X()

    def X(self):
        if self.lookahead == ",":
            self.match(",")
            self.F()
        else:
            pass # X -> ε
def main():
    input_string = input("Ingresa la cadena a analizar: ")
    tokens = input_string.split()
    parser = Parser(tokens)
    try:
        parser.S()
        print("\nLa cadena es válida.")
    except ValueError:
        print("\nLa cadena no es válida.")

def archivo():
    file = open("/Users/acer/Pictures/PYTHON/datux/Tareas/Tareas/Tarea2/Tareav2/filetextog.txt") #poner ruta propia
    a=file.read()
    #exp=a
    program = a.split("\n")
    lista=[]
    defi=[]
    for linea in program:
        item=linea.split(sep=" ")
        lista.append(item)
    for sub_lista in lista:
        for elemento in sub_lista :
            defi.append(elemento)
    print('\n')
    print(defi)
    parser = Parser(defi)
    try:
        parser.S()
        print("\nLa cadena es válida.")
    except ValueError:
        print("\nLa cadena no es válida.")

#main()

msgleer = """\nElija como desea analizarlo (separar cada palabra o simbolo):

    a) Leer en consola
    b) Leer archivo de texto

    """
print(msgleer)
opc=input('Ingresar la opción: ').upper()
print('Opción elegida: ',opc)

if(opc!='A' or opc!='B'):
    if opc=='A':
        main()
    elif opc=='B':
        archivo()
    else:
        print('OPCION INVÁLIDA')
else:
    print('OPCIÓN INVALIDA')