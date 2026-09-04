A simple machine safety-check system.
Compares input temperature and pressure against fixed maximum thresholds (max_temp = 80, max_pressure = 150).
validate() returns 'SAFE TO OPERATE' or 'SHUTDOWN REQUIRED' accordingly.
Concepts used: functions, conditional logic.

code:
     
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
