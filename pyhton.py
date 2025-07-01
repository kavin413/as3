valid= False
while not valid:
    try:
        n=int(input("enter a number of your choice: "))
        while n%2==0:
          print("bye")
          valid= True
    except ValueError:
        print("the number is not even ")
        