max_temp=80
max_pressure=150

temp=int(input('ENTER THE TEMPERATURE :'))
pressure=int(input('ENTER THE PRESSURE:'))

def validate():
     if temp<=max_temp and pressure<=max_pressure:
         return 'SAFE TO OPERATE '

     else:
         return 'SHUTDOWN REQUIRED'

r=(validate())
print(r)
