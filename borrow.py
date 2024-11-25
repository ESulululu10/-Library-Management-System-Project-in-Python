import datetime

def borrow():
    total=0
    bookName=""
    dictionary_books={}
    time = datetime.datetime.now()

    countA="False"
    countB="False"
                
    while countA=="False":
        borrower_name = input("Please enter the name of borrower: ")
        try:
            int(borrower_name)
            print("Please enter a valid name: ")
        except:
            countA="True"
            
    while countB=="False":
        continuation ="False"
        while countA =="True":
            try:
                book_id = int(input("Please enter the book ID: "))
                if 1<=book_id<6:
                    countA ="False"
                else:
                    print("Invalid ID!!! \nPlease enter the correct ID: ")
            except:
                print("Please enter a valid book ID: ")

        while countA =="False":
            try:
                quantity = int(input("Please enter the book's quantity you would like to borrow: "))
                countA ="True"
            except:
                print("Please enter a valid value: ")    


        file1 =open("books.txt","r")
        s=1
        for line in file1:
            line=line.replace("\n","")
            dictionary_books[s]= line.split(",")
            s=s+1
            
        v=1
        while v<=10:
            if book_id==v:

                h=dictionary_books[v]
                if int(h[2]) <= 0 :
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("\tBook is not available.")
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                elif int(h[2])< 6:
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("\tBook is available.")
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                else:
                    cost = float(h[3].replace("$",""))* quantity
                    total=total+cost
                    remaining = int(h[2]) - quantity
                    m=1
                    n=""

                file2=open("books.txt","r")
                m = 1
                n = ""
                remaining = int(h[2]) - quantity
                for line in file2:
                    if book_id==m:
                        p=line.replace(h[2],str(remaining))
                        n=n+p
                    else:
                        n=n+line
                    m=m+1
                    
                file3=open("books.txt","w")
                file3.write(n)
                while continuation =="False":
                    more = input("\nEnter 'y' if the person wants to borrow another books: ")
                    bookName = bookName + h[0] + "\n"
                    if more.lower()=="n":
                        Borrow=open("Borrow_.txt","w")
                        Borrow.write(borrower_name +"\n"+ bookName +str(time)+"\n"+"$"+str(total))
                        print("\n-----------Customer Details----------")
                        print("\nName of the borrower: "+ borrower_name)
                        print("List of the book borrowed:\n"+ bookName)
                        print("Total cost: ",total)
                        print("Date and Time: "+time.strftime("%Y-%M-%D  %H:%M:%S"))
                        continuation="True"
                        countB="True"
                    elif more.lower()=="y":
                        countA = "True"
                        continuation="True"
                        countB="False"
                    else:
                        print("Please enter 'y' for yes and 'n' for no: ")
            v = v + 1
                    
            
