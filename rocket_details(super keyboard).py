# A simple Python OOP project through a Falcon 9 rocket example.

# concepts involed:
# showing parent and child classes, constructors, and super()

#code
class components():
    def __init__(self,engine,booster,material,fuel):
        self.engine=engine
        self.booster=booster
        self.material=material
        self.fuel=fuel

class rocket(components):
    def __init__(self,rocket,launch_area,time,engine,booster,material,fuel):
        self.rocket=rocket
        super().__init__(engine,booster,material,fuel)
        self.launch_area=launch_area
        self.time=time

obj=rocket('FALCON-9','AMERICA-FLORIDA','4.00 am','SEMI-CRYOGENIC','SOLID','CARBON FIBRE','OXIDIZER+HYDROCARBON(KEROSENE)')

print('ROCKET:',obj.rocket)
print('COMPONENTS:')
print('=>ENGINE:',obj.engine)
print('=>BOOSTER:',obj.booster)
print('=>MATERIAL:',obj.material)
print('=>FUEL:',obj.fuel)
print('AREA:',obj.launch_area)
print('BOOSTER:',obj.booster)
        
        
 


        



     

        

