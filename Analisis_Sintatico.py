# Estado inicial
estado = 0  # empieza el programa si o si con whencuando
with open("Programa.txt", "r",encoding='utf-8') as Programa:
    Primera_linea = Programa.readline()
    
    
if Primera_linea == "whencuando": # si lo que se escribio es igual a whencuando
    print("Inicio correcto")
elif Primera_linea != "whencuando":
    print("Error: no hay 'whencuando'")
    
    
    
    
    
"""print("Escribe tu programa. welcome to C-MAMUT.")
while True:
    linea = input().strip()

    if estado == 0:  # si estado es igual a 0
        if linea == "whencuando": # si lo que se escribio es igual a whencuando
            print("Inicio correcto")
            estado += 1 # se le suma 1 al estado 
        else:
            print("Error: no hay 'whencuando'")

    elif estado == 1:  
        if linea.startswith("var "):
            # quitamos el "var " y vemos el primer caracter del Declaracion
            Declaracion = linea[4:].strip() # vemos que declara el ususario
            if "=" in Declaracion and Declaracion[0].isalpha() and Declaracion[0].isupper():
                print("Declaración de variable correcta")
                
            else:
                print("Error de sintaxis en esta línea")
                
        elif linea.startswith("plox "):
            print("Entrada de variable correcta")
            
        elif linea.startswith(":v"):
            print("Impresión correcta")
            
        elif linea.startswith("xdxd") & linea.endswith("xdxd"):
            print("Programa finalizado correctamente")
            break
        
        else:
            print("Error de sintaxis en esta línea") """