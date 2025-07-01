valid= False
while not valid:
    try:
        n=int(input("enter a number of your choice:"))
        n%2==0
        print("bye")
    except:
        print("the number is not even ")
        