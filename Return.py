import datetime
def Return():
    time=datetime.datetime.now()
    bookName=""
    dictionary_books={}
    numberOfDays=10
    charge=5
    totalCharge=0
    countA="False"
    countB="False"
    while countA=="False":
        borrower_name=input("Enter the name of the person who wants to return book: ")
        try:
            int(borrower_name)
            print("Please enter a valid name: ")
        except:
            countA="True"

    while countB=="False":
        continuation="False"
        while countA=="True":
            try:
                book_id =int(input("Please enter the book ID: "))
                if 1 <= book_id <= 10:
                    countA="False"
                else:
                    print("Invalid ID!!! \nPlease enter the correct ID: ")
            except:
                print("Please enter the valid book ID: ")

        while countA=="False":
            try:
                quantity=int(input("Please enter the book's quantity that you would like to return: "))
                countA="True"
            except:
                print("Please enter the valid value: ")


        file1=open("books.txt","r")
        s=1
        for line in file1:
            line=line.replace("\n","")
            dictionary_books[s]=line.split(",")
            s=s+1

        h=dictionary_books[book_id]
        remaining=int(h[2])+quantity
        n=""
        m=1

        file2=open("books.txt","r")
        for line in file2:
            if book_id==m:
                t=line.replace(h[2],str(remaining))
                n=n+t
            else:
                n=n+line
            m=m+1

        file3=open("books.txt","w")
        file3.write(n)

        w=int(input("Please enter the number of days that the book has been borrowed: "))
        if w > numberOfDays:
            late = w-numberOfDays
            totalCharge=((charge)*(late))
            print("You are",late,"days late to return the book. You will be charged $" ,totalCharge,".")
        else:
            print("Thank you for returning the book in time.")
            
        while continuation =="False":
            more=input("If you want to return more books, enter 'y': ")
            bookName=bookName+h[0]+"\n"
            if more.lower()=="n":
                print("\n------------Details of Returner--------------")
                print("\nName of the person who returned book: "+borrower_name)
                print("List of the book returned:\n"+ bookName)
                print("Charge:",totalCharge)
                print("Date and Time: "+time.strftime("%Y-%M-%D  %H:%M:%S\n"))
                Return=open("Return.txt","w")
                Return.write(borrower_name+","+h[0]+","+str(time)+"\n")
                continuation="True"
                countB="True"
            elif more.lower()=="y":
                continuation="True"
                countB="False"
                countA="True"
            else:
                print("Please enter 'y' for yes and 'n' for no: ")
                

                
