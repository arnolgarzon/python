
print (" WORLD CRAFT ".center(50,"#")+"\n")
print ('Bienvenid@ al mundo de WORL CRAFT digita una opcion: ')

def pedirNumero():

  
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Elige una opcion: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
  
#menu 
    print ("1. Usuario nuevo")
    print ("2. Usuario registrado")
    print ("3. Salir")
    
     
    print ("\n")
    
 #funcion
    opcion = pedirNumero()
 
    if opcion == 1:
        print("\n")
        import userNew
    elif opcion == 2:
        import userOld
    
    elif opcion == 3:
        salir = True
    else:
        print ("Introduce una opcion valida")
 
print ("Fin")

 

import users  # importación del archivo en donde se encuentra la función para comparar con los usuarios ya registrados

# --- RECUERDEN QUE DEBEN PRIMERO SOLICITAR EL CODIGO CDIA Y VALIDAR QUE CUMPLA CON LAS CONDICIONES, UNA VEZ VERIFICADO GENERAN UNA VARIABLE QUE ALMACENE EL CDIA Y LO ENVÍAN COMO ARGUMENTO PARA LA FUNCIÓN DESCRITA ABAJO


