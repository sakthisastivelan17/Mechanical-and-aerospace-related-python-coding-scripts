 Simulates logging and analyzing aircraft engine test data.
Takes RPM, temperature, and fuel consumption readings for 5 engine tests and writes them to engine_test.txt.
Reads the file back and calculates the highest, lowest, and average values for each parameter.
Lets the user search for a specific RPM value in the recorded data.
Appends a new engine test entry to the file and prints the fully updated report.
Concepts used: file I/O (open, read, write, append), loops, lists, aggregate calculations.
                    
code :
# writing the file 
file=open('engine_test.txt','w')

for i in range (1,6):
    print()
    print('engine test no:',i)
    erpm=int(input('enter the engine rpm:'))
    etemp=int(input('enter the engine temperature:'))
    efuel=int(input('enter the engine fuel consumption:'))
    print()
    file.write(str(erpm)+','+str(etemp)+','+str(efuel)+'\n')

file.close()

#data process
file=open('engine_test.txt','r')

rpm_data=[]
temp_data=[]
fuel_data=[]

totr=0
countr=0
tott=0
countt=0
totf=0
countf=0

for line in file:
    data=line.strip().split(',')
    rpmc=int(data[0])
    tempc=int(data[1])
    fuelc=int(data[2])

    totr=totr+rpmc
    countr=countr+1
    tott=tott+tempc
    countt=countt+1 
    totf=totf+fuelc
    countf=countf+1

    rpm_data.append(rpmc)
    temp_data.append(tempc)
    fuel_data.append(fuelc)

file.close()

#printing
maxr=max(rpm_data)
minr=min(rpm_data)
maxt=max(temp_data)
mint=min(temp_data)
maxf=max(fuel_data)
minf=min(fuel_data)

print()
print('    ---- aircraft engine report ----    ')
print()
print('total tests:',i)
print()
print('RPM ANALYSIS :')
print()
print('highest rpm =',maxr)
print('lowest rpm =', minr)
print('average rpm =',totr/countr)
print()
print('TEMPERATURE ANALYSIS :')
print()
print('highest temp =',maxt)
print('lowest temp =', mint)
print('average temp=',tott/countt)
print()
print('FUEL ANALYSIS :')
print()
print('highest fuel   =',maxf)
print('lowest fuel  =', minf)
print('average fuel   =',totf/countf)

#search rpm
print()
rpms=int(input('enter the rpm value to search;'))
if rpms in rpm_data:
    print('rpm value found')
else:
    print('rpm not found')


#new engine test
file=open('engine_test.txt','a')

print()
print('<--enter the new engine test-->')
print()
new_erpm=int(input('enter the new rpm:'))
new_etemp=int(input('enter the new temperature(in°c):'))
new_efuel=int(input('enter the new fuel consumption (in litres):'))

file.write(str(new_erpm)+','+str(new_etemp)+','+str(new_efuel)+'\n')

file.close()

#new updated file
print()
print(' ---- updated report ---- ')
print()
file=open('engine_test.txt','r')

a=file.read()
print(a)

file.close()



            


       





