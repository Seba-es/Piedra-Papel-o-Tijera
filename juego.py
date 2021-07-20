""" Piedra papel o tijera
Casos posibles 7 : piedra papel(viceversa), papel tijera(viceverda), tijera piedra(vicerversa), empate
* Asociar un número con piedra, papel o tijera 
* Hacer que el número selecionado por el programa sea aleatorio
* Usar if, elif y else para saber cuando el usuario gana, empata o pierde
* Crear un mecanismo de validación en caso de que el usuario no ingrese los datos pedidos
"""

import random 
import sys

usuario = sys.argv[1].lower()
numero = random.randint(1,3)

if numero == 1:
    muestra = 'piedra'
elif numero == 2:
    muestra = 'papel'
elif numero == 3:
    muestra = 'tijera'
    
print(f'Computador juega {muestra}')    

if muestra == usuario:
    print('Empataste')
elif muestra == 'papel' and usuario == 'tijera':
    print('Ganaste')
elif muestra == 'piedra' and usuario == 'papel':
    print('Ganaste')       
elif muestra == 'tijera' and usuario == 'piedra':
    print('Ganaste')
elif muestra == 'tijera' and usuario == 'papel':
    print('Te ganó la computadora')
elif muestra == 'papel' and usuario == 'piedra':
    print('Te ganó la computadora')       
elif muestra == 'piedra' and usuario == 'tijera':
    print('Te ganó la computadora')        
    

if usuario != 'piedra' and usuario != 'papel' and usuario != 'tijera':
    print('Su argmumento no es válido, solamente esta permitido ingresar piedra, papel o tijera')