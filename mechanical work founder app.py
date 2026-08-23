workers = ['ramesh','suresh','kamla','raj','ruban',]
selections = []
print('----------------------------------worker founder---------------------------------')
print('type (find worker) to hire worker. if you want worker info type (worker info),to know list type (worker list)type without any mistakes')

def find_worker():
    print('available workers:', workers)
    a = input('enter the name to select: ')
    if a in workers:
        selections.append(a)
        print(selections)
    else:
        print('worker not found')

def worker_info():
    w=input('enter worker name to get info about him:')
    if w == 'ramesh':
        print('seeking role: lathe machine handler')
        print('experience: 3 years worked as co lathe handler in mec groups company')
    elif w == 'suresh':
        print('seeking role: data handler')
        print('expereince: 1 month worked as  inter in ISRO')
    elif w == 'kamla':
        print('seeking role: design engineer')
        print('experience: 12 years worked as design engineer in spacex')
    elif w =='raj':
        print('seeking role: co manager')
        print('experience: 30 years as manager in amman tmt')
    elif w =='ruban':
        print('seeking role: sales manager')
        print('experience: 15 years worked as sales manager in ggheert  company')
    else:
        print('person not found')

def worker_list():
    print(workers)

while True:
    q = input('what work you want? ')

    if q == 'find worker':
        find_worker()
    elif q == 'worker info':
        worker_info()
    elif q == 'exit':
        break
    elif q == 'worker list'
         worker_list()
    else:
        print('unknown command')

