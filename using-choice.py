1

def circle():
   
    r=int(input("enter your radius (r) : "))
    pi=3.14
    perimeter=2*pi*r
    print("perimeter of a",perimeter)
    
    # a=circle()
    # print(a)
def square():
    a=int(input("enter your side : "))
    b=4
    c=b*a
    print("perimeter of a square",c)
    
def book():
    d={} 
    def add():
        
            a=int(input("enter how many pairs: "))
            for i in range(a):
                k=int(input("enter book number : "))
                if k in d:
                    print(f"book number {k} is  already  exists.")
                    break
                else: 
                    v=(input("enter your name : "))
                    d[k]=v
                    print(f"book number : {k} ,book name: {v} ")
                print("created")
    def display():
                 print(d)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    def delete():
            k=int(input("enter your number: "))
            if k in d:
                     #   f=d[k]
                del d[k]
                
                print(f" book number: {k} - deleted ")
            else:
                print(f"book number : {k} - not exists") 
    def edit():
            k=int(input("enter book number: "))
            if k in d:
                f=d[k]
                v=(input("enter book name: "))
                d[k]=v 
            
                print(f"enter book number : {k},old value :{f} ,new value : {v} ")
            else:
                print(f"book number:{k} not exists") 
    while True:
            print("1:add Book  \n"
            "2:display Book  \n"
            "3:Delete Book\n"
            "4:Edit Book\n"
            "5:exit\n") 
            y=int(input("enter your choice: "))
            if y==5:
                break
            elif y==1:
                add()
            elif y==2:
                display()
            elif y==3:
                delete()
            elif y==4:
                edit()
while True:
    print("1:circle perimeter \n"
         "2:square perimeter\n"
         "3:book\n"
         "4:exit\n") 
    x=int(input("enter your choice: "))
    if x==4:
        break
    elif x==1:
        circle()
    elif x==2:
        square()
    elif x==3:
        book()
        
        
        
  