def message():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Hello and Welcome to the Library Management System ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
message()

def option():
    print("\nEnter '1' to borrow book")
    print("Enter '2' to return book")
    print("Enter '3' to exit \n")

continuation = True
while continuation == True:
    import read
    read.read()
    option()
    count = False
    while count == False:
        try:
            value = int(input("Please enter a value: "))
            count = True
        except:
            print("Please enter the valid number(1,2 or 3): ")
    if value==1:
        print("\nYou will now borrow a book.")
        import borrow
        borrow.borrow()
    elif value==2:
        print("\nYou will now return a book")
        import Return
        Return.Return()
    elif value==3:
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("  Thank you for using our library management system.")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        continuation = False
    else:
        print("\nPlease enter valid number(1,2 or 3): ")
        
    
