"""
Date: 31 December 2022
Author: Bulli shesharao
Project: Student library management system
"""


class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} AVAILABLE BOOKS ARE: ")
        for book in self.books:
            print(" ♦-- " + book)
        print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(
                f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
        else:
            track.append({name: bookname})
            print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN ON TIME.\n")
            self.books.remove(bookname)

    def returnBook(self, bookname):
        print("BOOK RETURNED : THANK YOU! \n")
        self.books.append(bookname)

    def donateBook(self, bookname):
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(bookname)


class Student():
    def requestBook(self):
        print("So, you want to borrow book!")
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        print("So, you want to return book!")
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        print("Okay! you want to doante book!")
        self.book = input("Enter name of the book you want to donate: ")
        return self.book


if __name__ == "__main__":

    Andhralibrary = Library(
        ["Science", "social", "Telugu", "Mathematics", "Geography", "microeconomics"])
    student = Student()
    track = []

    print("\t\t\t\t\t\t\t♦♦♦♦♦♦♦ WELCOME TO THE ANDHRA LIBRARY ♦♦♦♦♦♦♦\n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. exit the library\n""")

    while (True):
        # print(track)
        try:
            user_response = int(input("Enter your choice: "))

            if user_response == 1:  # listing
                Andhralibrary.displayAvailableBooks()
            elif user_response == 2:  # borrow
                Andhralibrary.borrowBook(
                    input("Enter your name: "), student.requestBook())
            elif user_response == 3:  # return
                Andhralibrary.returnBook(student.returnBook())
            elif user_response == 4:  # donate
                Andhralibrary.donateBook(student.donateBook())
            elif user_response == 5:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
            
            elif user_response == 6: #exit
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:              #catch errors
            print(f"{e}---> INVALID INPUT! \n")