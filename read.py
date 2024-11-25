
def read():
    print("--------------------------------------------------------------------")
    print("Book ID          Book-Name      Author       Quantity     Price  ")
    print("--------------------------------------------------------------------")
    file=open("books.txt","r")
    b=1
    for line in file:
        print("  ",b,"\t\t"+line.replace(",","\t"))
        b=b+1
    print("--------------------------------------------------------------------")

    file1=open("books.txt","r")
    dictionary_books={}
    s=1
    for line in file1:
        line=line.replace("\n","")
        dictionary_books[s]=line.split(",")
        s=s+1
    
    return dictionary_books
