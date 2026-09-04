file=open('marks_data.txt','w')

thermo=float(input('enter your thermodyanmics mark :')
som=float(input('enter your strength of mechanics mark:')
fm=float(input('enter your fluid mechanics mark:')
mt=float(input('enter your manufacturing technology mark:')

file.write(str(thermo)+'\n')
file.write(str(som)+'\n')
file.write(str(fm)+'\n')
file.write(str(mt)+'\n')

file.close()

file=open('marks_data.txt','r')

marks_list=[]
tot=0
count=0

for line in file:
      inter=int(line)
      tot=tot+inter
      count=count+1
      marks_list.append(inter)

file.close()

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", max(marks_list))


        




