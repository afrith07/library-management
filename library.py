class library():
    def __init__(self,list):
        self.book_list = list
        self.available_book_list = list[:]
        self.books_lent = {}

    def disavai(self):
        for book in self.available_book_list:
            print(book)

    def disall(self):
        for book in self.book_list:
            print(book)


    def bor(self,name,book):
        if book not in self.book_list:
            print("Incorrect book")
            return
        if book in self.available_book_list:
            self.books_lent.update({book:name})
            self.available_book_list.remove(book)
            print("Take the Book...")
        else:
            print("Book is already Taken by "+ self.books_lent[book])


    def ret(self,book):
        print("Thank you .visit again..")
        del self.books_lent[book]
        self.available_book_list.append(book)

    def quit(self):
        pass

if __name__ =="__main__":
    lib = library(["cs","it","ece","mech","civil"])
    print("Welcome to Library . Enter an Option. ")
    while True:
        print("1.Display available books")
        print("2.Display all books ")
        print("3.Borrow a book ")
        print("4.Return a Book")
        print("5.Quit ")
        user = int(input("enter an option :"))
        if user == 1:
            lib.disavai()
        elif user == 2:
            lib.disall()
        elif user == 3:
            name = input("Enter a user name : ")
            book = input("Enter a book name : ")
            lib.bor(name,book)
        elif user == 4:
            book = input("Enter the name of the Book")
            lib.ret(book)
        elif user == 5:
            break
        else:
            print("Invalid choices...")

