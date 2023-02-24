from collections import OrderedDict

def esterm(char):
    if(char.isupper() or char == "`"): 
        return False
    else:
        return True

def insertar(gram, lhs, rhs):
    if(lhs in gram and rhs not in gram[lhs] and gram[lhs] != "null"):
        gram[lhs].append(rhs)
    elif(lhs not in gram or gram[lhs] == "null"):
        gram[lhs] = [rhs]
    return gram
	
def iniciales(lhs, gram, gram_ini):
    rhs = gram[lhs]
    for i in rhs:
        k = 0
        flag = 0
        actual = []
        confirm = 0
        flog = 0
        if(lhs in gram and "`" in gram_ini[lhs]):
            flog = 1
        while(1):	
            check = []
            if(k>=len(i)):
                if(len(actual)==0 or flag == 1 or confirm == k or flog == 1):
                    gram_ini = insertar(gram_ini, lhs, "`")
                break				
            if(i[k].isupper()):
                if(gram_ini[i[k]] == "null"):
                    gram_ini = iniciales(i[k], gram, gram_ini)
                   # print("state ", lhs, "i ", i, "k, ", k, grammar_first[i[k]])
                for j in gram_ini[i[k]]:
                    gram_ini = insertar(gram_ini, lhs, j)
                    check.append(j)
            else:
                gram_ini = insertar(gram_ini, lhs, i[k])
                check.append(i[k])
            if(i[k]=="`"):
                flag = 1
            actual.extend(check)
            if("`" not in check):
                if(flog == 1):
                    gram_ini = insertar(gram_ini, lhs, "`")
                break
            else:
                confirm += 1
                k+=1
                gram_ini[lhs].remove("`")
    return(gram_ini)

def seguidoresRec(k, next_i, gram_seg, i, gram, start, gram_ini, lhs):
    if(len(k)==next_i):
        if(gram_seg[i] == "null"):
            gram_seg = seguidores(i, gram, gram_seg, start)
        for q in gram_seg[i]:
            gram_seg = insertar(gram_seg, lhs, q)
    else:
        if(k[next_i].isupper()):
            for q in gram_ini[k[next_i]]:
                if(q=="`"):
                    gram_seg = seguidoresRec(k, next_i+1, gram_seg, i, gram, start, gram_ini, lhs)		
                else:
                    gram_seg = insertar(gram_seg, lhs, q)
        else:
            gram_seg = insertar(gram_seg, lhs, k[next_i])

    return(gram_seg)

def seguidores(lhs, gram, gram_seg, start):
    for i in gram:
        j = gram[i]
        for k in j:
            if(lhs in k):
                next_i = k.index(lhs)+1
                gram_seg = seguidoresRec(k, next_i, gram_seg, i, gram, start, gram_ini, lhs)
    if(lhs==start):
        gram_seg = insertar(gram_seg, lhs, "$")
    return(gram_seg)

def verSimbenDic(dictionary):
    for key in dictionary.keys():
        print(key+"  :  ", end = "")
        for item in dictionary[key]:
            if(item == "`"):
                print("Epsilon, ", end = "")
            else:
                print(item+", ", end = "")
        print("\b\b")

def obtenerReglas(noterm, term, gram, gram_ini):
    for rhs in gram[noterm]:
        #print(rhs)
        for rule in rhs:
            if(rule == term):
                string = noterm+"~"+rhs
                return string
            
            elif(rule.isupper() and term in gram_ini[rule]):
                string = noterm+"~"+rhs
                return string
                
def gentablaanalisis(terms, noterms, gram, gram_ini, gram_seg):
    tabla_anali = [[""]*len(terms) for i in range(len(noterms))]
    
    for noterm in noterms:
        for term in terms:
            #print(term)
            #print(grammar_first[noterm])
            if term in gram_ini[noterm]:
                rule = obtenerReglas(noterm, term, gram, gram_ini)
                #print(rule)
                
            elif("`" in gram_ini[noterm] and term in gram_seg[noterm]):
                rule = noterm+"~`"
                
            elif(term in gram_seg[noterm]):
                rule = "Sync"
                
            else:
                rule = ""
                
            tabla_anali[noterms.index(noterm)][terms.index(term)] = rule
        
    return(tabla_anali)

def vertablaanalisis(tabla_anali, term, noterm):
    print("\t\t\t\t",end = "")
    for term in terms:
        print(term+"\t\t", end = "")
    print("\n\n")
    
    for noterm in noterms:
        print("\t\t"+noterm+"\t\t", end = "")
        for term in terms:
            print(tabla_anali[noterms.index(noterm)][terms.index(term)]+"\t\t", end = "")
        print("\n")


def analizar(expr, tabla_anali, terms, noterms):
    pila = ["$"]
    pila.insert(0, noterms[0])

    print("\t\t\tEncuentros\t\t\tPila\t\t\tEntrada\t\t\tAcciòn\n")
    print("\t\t\t-\t\t\t", end = "")
    for i in pila:
        print(i,  end = "")
    print("\t\t\t", end = "")
    print(expr+"\t\t\t", end = "")
    print("-")

    matched = "-"
    while(True):
        action = "-"

        if(pila[0] == expr[0] and pila[0] == "$"):
            break

        elif(pila[0] == expr[0]):
            if(matched == "-"):
                matched = expr[0]
            else:    
                matched = matched + expr[0]
            action = "Encontrado "+expr[0]
            expr = expr[1:]
            pila.pop(0)

        else:
            action = tabla_anali[noterms.index(pila[0])][terms.index(expr[0])]
            pila.pop(0)
            i = 0
            for item in action[2:]:
                if(item != "`"):
                    pila.insert(i,item)
                i+=1

        print("\t\t\t"+matched+"\t\t\t", end = "")
        for i in pila:
            print(i,  end = "")
        print("\t\t\t", end = "")
        print(expr+"\t\t\t", end = "")
        print(action)





#################################             Main_Driver             #################################





gram = OrderedDict()
gram_ini = OrderedDict()
gram_seg = OrderedDict()

f = open("/Users/acer/Pictures/PYTHON/datux/Tareas/Tareas/Tarea2/Tareav1/grammar2.txt")

for i in f:
    i = i.replace("\n", "")
    lhs = ""
    rhs = ""
    flag = 1
    for j in i:
        if(j=="~"):
            flag = (flag+1)%2
            continue
        if(flag==1):
            lhs += j
        else:
            rhs += j
    gram = insertar(gram, lhs, rhs)
    gram_ini[lhs] = "null"
    gram_seg[lhs] = "null"

print("Gramàtica\n")
verSimbenDic(gram)

for lhs in gram:
    if(gram_ini[lhs] == "null"):
        gram_ini = iniciales(lhs, gram, gram_ini)
        
print("\n\n\n")
print("Iniciales\n")
verSimbenDic(gram_ini)


start = list(gram.keys())[0]
for lhs in gram:
    if(gram_seg[lhs] == "null"):
        gram_seg = seguidores(lhs, gram, gram_seg, start)
        
print("\n\n\n")
print("Seguidores\n")
verSimbenDic(gram_seg)


noterms = list(gram.keys())
terms = []

for i in gram:
    for rule in gram[i]:
        for char in rule:
            
            if(esterm(char) and char not in terms):
                terms.append(char)

terms.append("$")

#print(noterms)
#print(terms)


print("\n\n\n\n\t\t\t\t\t\t\tTabla de anàlisis\n\n")
tabla_anali = gentablaanalisis(terms, noterms, gram, gram_ini, gram_seg)
vertablaanalisis(tabla_anali, terms, noterms)


#expr = input("Enter the expression ending with $ : ")
#expr = "i+i*i$"
expr = "si"+"{"+"};$"

print("\n\n\n\n\n\n")
print("\t\t\t\t\t\t\tAnalizando Expresiòn\n\n")
try:
    analizar(expr, tabla_anali, terms, noterms)
    print("\nReconoce\n")
except:
    print("\nNo reconoce\n")