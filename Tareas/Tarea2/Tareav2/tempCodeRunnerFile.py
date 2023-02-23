
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
        if self.lookahead == "identifier":
            self.match("identifier")
        else:
            pass # A -> ε

    def B(self):
        if self.lookahead in ["int", "float", "double", "char", "bool", "string"]:
            self.D()
            while self.lookahead == "identifier":
                self.D()
        else:
            pass # B -> ε

    def D(self):
        self.E()
        self.match("identifier")
        self.match(";")

    def E(self):
        if self.lookahead in ["int", "float", "double", "char", "bool", "string"]:
            self.match(self.lookahead)
        else:
            raise ValueError("Error de sintaxis")

    def C(self):
        if self.lookahead == "identifier":
            self.F()
        else:
            pass # C -> ε

    def F(self):
        self.match("identifier")
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
        print("La cadena es válida.")
    except ValueError:
        print("La cadena no es válida.")

main()