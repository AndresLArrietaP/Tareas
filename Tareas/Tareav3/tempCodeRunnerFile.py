from scanner import Scanner

def main():
    estado = 0
    print ("""+-------------------------------------+
    |    Ingrese una cadena a evaluar:    |
    +-------------------------------------+""")
    cadena = input()
    #exp=cadena+" $"
    s=Scanner(cadena)
    tokens=s.ScanAll()
    print(tokens)

if __name__=='__main__':
    main()