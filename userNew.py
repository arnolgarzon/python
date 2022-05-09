
cdia = input("Digita tu cdia: ")
c = cdia.upper()
#condicional para validar las reglas establecidas para crear el CDIA
if (c[0] != c[9]) and (len(c) == 10) and c[5] == "@" and c.find("+") != -1 and c.count("k")<=3 and (c.find("0") == -1 and c.find("1") == -1 and c.find("2") == -1 and c.find("3") == -1 and c.find("4") == -1 and c.find("5") == -1 and c.find("6") == -1 and c.find("7") == -1 and c.find("8") == -1 and c.find("9") == -1) and (c.find("?") != -1 or c.find("=") != -1 or c.find("&") != -1):
  print("cdia valido")
  def user():
    user=c
    return user
else:
  print("cdia invalido, ingrese de nuevo")

import users
validar = users.buscar_cdia(
    user()
)  # ESTO ES UN EJEMPLO DE COMO DEBEN LLAMAR LA FUNCIÓN PARA VALIDAD USUARIOS YA EXISTETES
if validar == False:
  fecha = input('Ingrese fecha de nacimiento en formato DD/MM/AAAA: ')
  def edad():
    edad = 2022 - int(fecha[4:])
    return edad
  if edad() > 12:
    alias = input('Ingresa tu alias, debe tener minimo 5 caracteres sin espacio: ')
    haJugado = input('Ya has jugado worldCraft? (Si o No): ')
    haJugado_lower = haJugado.lower()
    
    
    if len(alias) > 5 and edad() < 16 and haJugado_lower == "si":
      nivel = input('Hasta que nivel llegaste? (1 - 100): ')
      print(nivel)
    elif len(alias) > 5 and edad() < 16 and haJugado_lower == "no":
      print("No has jugado antes, nivel 2")
    elif len(alias) > 5 and edad() >= 16 and haJugado_lower == "no":
      print('No ha jugado, nivel 1')
    else:
      print('Alias incorrecto')
  else:
    print('No tienes la edad para jugar este juego')
    quit()
else:
  print('El cdia esta en la lista')
# ESTA FUNCIÓN ESTA GENERADA EN EL MODULO users.py OJOOOO NO MODIFICARLA, ESTA FUNCIÓN LES RETORNA UN VALOR FALSO O VERDADERO DESPUES DE COMPARAR CON LOS USUARIOS YA REGISTRADOS.

