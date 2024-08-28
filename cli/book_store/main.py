"""_
this program keep track of all our books
version 1.0.0
date: ../../....
"""

def main():
    
    try:
        
    # initialize books list
        bookslist = []
        infile = open("thebookslist.txt","r")   
        line = infile.readline()
        while line:
            bookslist.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
        
    except FileNotFoundError:
        print("the <thebooklist.txt> file is not found")
        print("starting a new book list")
        bookslist = []
        
    
    
    choice = 0
    while choice !=4:
        print(" *** Books Manager *** ")
        print("1) add a book")
        print("2) lookup a book")
        print("3) display all books")
        print("4) quit book manager")
        choice = int(input())
        
        if choice == 1:
            print("adding a book...")
            nBook = input("enter the name of the book>>> ")
            nAuthor = input("enter the name of the author>>> ")
            nPages = input("enter the name of the number of pages>>> ")
            bookslist.append([nBook,nAuthor,nPages])
            
        elif choice == 2:
            print("looking up for a book...")
            keyword = input("enter search term: ")
            for book in bookslist:
                if keyword in book:
                    print(book)
                    
        elif choice == 3:
            print("displaying all books...")
            for i in range(len(bookslist)):
                print(bookslist[i])
                
        elif choice == 4:
            print("quiting books manager")
    print("program ternimated")
            
            
    # saving to txt file
    
    outfile = open("thebookslist.txt","w")   
    for book in bookslist:
        outfile.write(",".join(book)+ "\n")
    outfile.close()    





    
if __name__ == "__main__":
    main()
    