"""  Proyecto -> Inventario de una heladeria <-
** Autor:
* @ J Sebastian S
**
 
###################################################
                   Menu principal
#######################################################
"""
# Funcion para mostrar el menu
def menuPrincipal():
  print("Seleccione una opcion del (1 - 5) o q para salir")
  print("1. Comprar")
  print("2. Agregar un nuevo produncto")
  print("3. Ver inventario")
  print("4. Agregar al inventario")
  print("5. Total de ventas del dia")
  print("q. Salir")
  print()  
 
# Funcion para manipular las entradas y condiciones del menu principal
def condicionesMenuPrincipal():
  entrada = input()
  if entrada == "1":
    compra()
  elif entrada == "2":
    nuevoproducto()
  elif entrada == "3":    
    inventario()
  elif entrada == "4":
    AgregarInventario()
  elif entrada == "5":
    ventasDiarias()
  elif entrada == "q":
    salir() 
  
# Funcion salir del programa
def salir():
  return exit()       
 
# Funcion para declarar las variables globales del programa
def main_2():
  """ Listas globales
  Listas de productos como variables globales, organizados de la siguiente manera:
  helados = [ [producto, valor, porciones], [producto, valor, porciones], [producto, valor, porciones] ]
  coberturas = [ [producto, valor, porciones], [producto, valor, porciones], [producto, valor, porciones] ]
  ventas = [] # Va guardando las ventas de cada transaccion realizada en la funcion comprar
  """
  global helados, coberturas, ventas
  helados = [ ["Vainilla", 3000, 12], ["Chocolate", 3500, 50], ["Fresa", 4000, 20] ]
  coberturas =[ ["M&Ms",1500, 30], ["Galletas",1000, 40], ["Mani", 2000, 20] ]
  ventas = [0]
 
# Funcion principal que ejecuta todo el programa
def main():
  menuPrincipal()
  condicionesMenuPrincipal()   
 
 
""" ###################################################
                     1. Comprar
#######################################################
"""
# Funcion para que los usuarios compren helados y coberturas
def compra():
  precioTotal = 0
  print("Nueva venta:")
  print("Escoge un sabor:")
  impHelados()
  print()
  num = int(input()) - 1
  print("Usted selecciono:")
  print(str(num+1) + ")", helados[num][0], " "*(20-len(helados[num][0])), helados[num][1]," ", helados[num][2] )
  print()
  print("¿Cuantas porciones?")
  porcion_1 = int(input())
  precioTotal += (helados[num][1]*porcion_1)
  helados[num][2] -= porcion_1
  print()
  print("¿Desea cobetura?  (s/n)")    
  x = input()
  print()  
  if x == "s":
    print("Escoje la cobertura:")
    impCoberturas()
    print()
    num = int(input()) - 1
    print("Usted selecciono:")
    print(str(num+1) + ")", coberturas[num][0], " "*(20-len(coberturas[num][0])), coberturas[num][1]," ", coberturas[num][2] )
    print()
    print("¿Cuantas porciones?")
    porcion_2 = int(input())
    precioTotal += (coberturas[num][1]*porcion_2)
    coberturas[num][2] -= porcion_2
    print()
    print("Total a pagar:", precioTotal)
  elif x == "n":
    print("Total a pagar:", precioTotal)
  ventas.append(precioTotal)
  print()
  main()  
  
 
""" ###################################################
             2. Agregar un nuevo producto
#######################################################
"""   
# Funcion para agregar un nuevo producto (helado o cobertura) al inventario
def nuevoproducto():
  print("1. Helado")
  print("2. Cobertura")
  print("q. Salir")
  print()
  
  entrada = input()
  if entrada == "1":
    print("Ingrese el nombre del producto")
    producto = input()
    print()
    print("Ingrese el valor de la porcion")
    valor = int(input())
    print()
    print("Ingrese el numero de porciones disponibles")
    porciones = int(input())
    print()
    helados.append([producto, valor, porciones])
  elif entrada == "2":
    print("Ingrese el nombre del producto")
    producto = input()
    print()
    print("Ingrese el valor de la porcion")
    valor = int(input())
    print()
    print("Ingrese el numero de porciones disponibles")
    porciones = int(input())
    print()
    coberturas.append([producto, valor, porciones])
  main()
 
 
""" ###################################################
                 3. Ver inventario
#######################################################
"""  
# Funcion para borrar los helados y coberturas con 0 porciones
def borrar():
  indicesHelados = []
  indicesCoberturas = []
  for a in range(len(helados)):
    if helados[a][2] == 0:
      indicesHelados.append(a)
  for b in range(len(coberturas)):
    if coberturas[b][2] == 0:
      indicesCoberturas.append(a)
  for c in indicesHelados:
    del(helados[c])           
  for d in indicesCoberturas:
    del(coberturas[d])
 
# Funcion para imprimir los helados con 1 o más porciones
def impHelados():
  borrar()
  for a in range(len(helados)):
    print(str(a+1) + ")", helados[a][0], " "*(20-len(helados[a][0])), helados[a][1]," ", helados[a][2] ) 
 
# Funcion para imprimir las coberturas con 1 o más porciones
def impCoberturas():
  borrar()
  for b in range(len(coberturas)):
    print(str(b+1) + ")", coberturas[b][0], " "*(20-len(coberturas[b][0])), coberturas[b][1]," ", coberturas[b][2] )
 
# Funcion para imprimir el inventario      
def inventario():
    borrar()
    print("Helados")
    impHelados()
    print()
    print("Coberturas")
    impCoberturas()
    print()
    main()
 
 
""" ###################################################
                4. Agregar al inventario
#######################################################
"""  
# Funcion para agregar el total de porciones de helados o coberturas
def AgregarInventario():
  print("Tipo de producto (1 o 2)")
  print("1. Helado")
  print("2. Cobertura")
  print("q. Salir")
  
  entrada = input()
  print()
  if entrada == "1":
    print("Seleccione un producto")  
    impHelados()
    num = (int(input())) -1
    print()
    print("Usted selecciono:")
    print(str(num+1) + ")", helados[num][0], " "*(20-len(helados[num][0])), helados[num][1]," ", helados[num][2] )
    print()
    print("Ingrese la cantidad de porciones a registrar:")
    helados[num][2] = int(input())
    print()
  elif entrada == "2":
    print("Seleccione un producto")  
    impCoberturas()
    num = (int(input())) -1
    print()
    print("Usted selecciono:")
    print(str(num+1) + ")", coberturas[num][0], " "*(20-len(coberturas[num][0])), coberturas[num][1]," ", coberturas[num][2] )
    print()
    print("Ingrese la cantidad de porciones a registrar:")
    coberturas[num][2] = int(input())
    print()
  main()   
              
 
""" ###################################################
              5. Total de ventas del dia
#######################################################
""" 
# Funcion para ver o reiniciar el total de ventas diarias
def ventasDiarias():
  total = 0
  global ventas
  for e in ventas:
    total += e 
  print("Total ventas del día:", total)
  print() 
  print("Oprima s para reiniciar las ganancias diarias o n para salir")
  if input() == "s":
    ventas = []
  print()
  main()
 
main_2()
main()
