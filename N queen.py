print("IF U WANT TO DELETE PREVIOUS ONE OF THE INPUT. ENTER 'delete' IN 'row' INPUT")
print('ROW AND COLUMN ENTRIES STARTING FROM 0')
n=int(input('no. of grids'))
print('LEVEL',n,' STARTED')
def GAME(n):
    a=n
    l=[]
    def deleteinput():
        l.remove(l[-1])
    def deletepriviousentry():
        x=int(input('deleterow'))
        y=int(input('deletecolumn'))
        l.remove([x,y])
        print('DELETED')

    def game(a):
        x=input('row')
        if x=='delete':
            deletepriviousentry()
            return game(a+1)
        y=int(input('column'))
        z=int(x)
        if z<n and y<n:
            l.append([z,y])
            if a==n:
                print('queen',a,'is added')
            else:
                for j in l[0:-1]:
                    if block(j[0],j[1])==0:
                        deleteinput()
                        print('enter again')
                        return game(a)
                        break
                else:
                    print('queen ',(a),'is added')
            if a-1==0:
                print('YOU COMPLETED LEVEL',n,' SUCCESSFULLY')
                print('NEXT LEVEL',n+1,' STARTED')
                a=n+1
                return GAME(n+1)
            else:
                return game(a-1)
        else:
            print('ENTER THE ROW AND COLUMN ONE LESS THAN LEVEL NUMBER')
            return game(a)

    def block(r,c):         #after input blocked boxex
        k=l[-1]
        x=k[0]
        y=k[1]
        t=[]   #POSSIBLE POSITIONS LIST
    
        for i in range(min(r,c)+1):
            (a,b)=(r,c)
            (a,b)=(r+i,c-i)
            t.append([a,b])
            t.append([b,a]) 
        if (x-y)==r-c or  x==r or y==c or [x,y] in t:
             return 0
        else:
            return 1
    game(a)
GAME(n)
