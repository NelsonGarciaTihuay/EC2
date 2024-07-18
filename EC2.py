archivo = open("calificaciones.txt", "a")

nombre = input("Ingrese nombre completo del estudiantes: ")
archivo.write(nombre + '\n')

while(True):
    try:
        n1 = float(input("Ingrese primera calificacion: "))
        archivo.write('Primera nota:% s' %n1 + '\n')
        break
    except:
        print("Debes ingresar numeros. Intentelo de nuevo.")

while(True):
    try:
        n2 = float(input("Ingrese segunda calificacion: "))
        archivo.write('Segunda nota:% s' %n2 + '\n')
        break
    except:
        print("Debes ingresar numeros. Intentelo de nuevo.")

while(True):
    try:
        n3 = float(input("Ingrese tercera calificacion: "))
        archivo.write('Tercera nota:% s' %n3 + '\n')
        break
    except:
        print("Debes ingresar numeros. Intentelo de nuevo.")

while(True):
    try:
        n4 = float(input("Ingrese segunda calificacion: "))
        archivo.write('Cuarta nota:% s' %n4 + '\n')
        break
    except:
        print("Debes ingresar numeros. Intentelo de nuevo.")

        
promedio = (n1+n2+n3+n4)/3
archivo.write('Promedio:% s' %promedio + '\n' )
print("El promedio es: ", promedio)
print("<---------------------->")
lista = input("Desea ver la lista de calificaciones SI/NO: ")

if lista == 'si':
    archivo = open("calificaciones.txt", "r")
    print(archivo.read())
elif lista == 'no':
    print("Fin del programa.")


