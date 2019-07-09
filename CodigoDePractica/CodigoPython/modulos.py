#modulo conjunto de funciones(importar o llamar librerias de python)

import datetime
hoy = datetime.date.today()
print(hoy)

#form datetime import date
#hoy2 = date.today()
#print(hoy2)


import time 
estampatemporal= time.time()
print(estampatemporal)

import validador
from validador import validate_email

email = 'pruebueba.com'
if validate_email(email):
   print('el correo esta bien escrito')
else:
   print('el correo esta mal escrito')

