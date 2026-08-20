import time
time.sleep(1)
print('---------------------------------------------------------------------------')
print('            WELCOME TO MECHANICAL WORKSHOP EDITOR             ')
print()
print()
print('SMALL INFO : THIS IS AN BETA 1.0 VERSION ')
print('SO BUGS AND GLICTH MAY HAPPEN WE WILL IMPROVE ON FURTHER VERSIONS.')
print('IN THIS APP :YOU CAN ADD,REMOVE,CHECK ITEMS,SORT,MODIFY,PRINT,CLEAR.')

       
      
machines=[]
num_file=[]

while True:
       print()
       method=input('TELL THE WORK TO DO :').strip().lower()
       print()
       print('ooooo LOADING ooooo')
       import time
       time.sleep(1)
       print()
     
       if method == 'add':

            while True:
                   machine=input('ENTER THE MACHINE NAME TO ADD:')
                   machines.append(machine)

                   print('CURRENT MACHINES:',machines)

                   again=input('ADD ANOTHER MACHINE NAME (YES/NO):').strip().lower()

                   if again=='no':
                          break
                   
  
       
       elif method == 'remove':
             
             if len(machines)==0:
                
                print('xxx NO MACHINES AVAILABLE TO REMOVE xxx')
                

             else:
                  
                  have=input('ENTER THE MACHINE TO REMOVE:')
                  print()
                  import time
                  time.sleep(1)
                  print('oooo LOADING oooo')
                  print()
                
          
                  
     
                  if have in machines :
                     machines.remove(have)
                     print(machines)
                 
               
                  else:
                      print()
                      print('xxx NO MACHINES AVAILABLE TO REMOVE xxx')
       
       elif method== 'check':
                  
                

                  if len(machines)==0:
                      print('xxx NO MACHINES AVAILABLE TO CHECK xxx')

                  else:
                       print(machines[(int(input('ENTER THE POSITION TO CHECK:')))])

       elif method=='clear':
              machines.clear()
              print(machines)


       elif method=='sort':
             
               if len(machines)==0:
                  print('xxx NO MACHINES AVAILABLE TO SORT xxx')

               else :
                    machines.sort()
                    print(machines)

       elif method=='modify':

              if len(machines)==0:
                     print('xxx NO MACHINES AVAILABLE TO SORT xxx')

              else:
                     modifier=int(input('ENTER THE INDEX TO MODIFY:'))
                     letter=input('ENTER THE NAME TO MODIFY:')
                     machines[modifier]=letter
                     print(machines)

       elif method=='exit':
            
            print('EXITING.....')
            print()
            break

       elif method=='open num file':

              print('NUM FILE OPENED:',num_file)

       elif method=='max':

              print('ENTER THE NUMBER TO FIND MAX:',max(num_file))

    
       elif method=='i':
              inx=int(input('ENTER THE NUMER TO INSERT:'))
              num_file.append(inx)
              print()
              print('CURRENT NUMBERS:',num_file)
              print()

              again=(input('DO YOU WANT TO INSERT (YES/NO):')).strip().lower()

              if again=='no':
                  break

       else:
               
               print('xxxxx ERROR xxxxx')
      
