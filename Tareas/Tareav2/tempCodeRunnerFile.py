import re

cadena =input("Ingrese la cadena:")
patron=re.compile(r'((\s*(void|int|float|double|char|bool|string){1}\s+([\$_a-zA-Z]+[\$_\w]*){1}\s*(\(){1}\s*(((int|float|double|char|bool|string){1}\s+([\$_a-zA-Z]+[\$_\w]*){1}\s*(\,){1}\s*)*((int|float|double|char|bool|string){1}\s+([\$_a-zA-Z]+[\$_\w]*){1}\s*){1}){0,1}(\)){1}\s*(\{){1}\s*(\}){1}\s*))*\s*(main){1}\s*(\(){1}\s*(\)){1}\s*(\{){1}\s*(\}){1}')

coincidencias=patron.fullmatch(cadena) 

print(coincidencias)

if coincidencias:
    print("La cadena " + cadena +" se acepta")
else:
    print("La cadena " + cadena +" no se acepta")