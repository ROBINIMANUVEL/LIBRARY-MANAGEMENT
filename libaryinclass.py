def out():
    print("Exiting...")


class User:
    books = {'a': 10, 'b': 10, 'c': 10, 'd': 4}

    def __init__(self, name, phone_no, no_of_books=0, books_taken=None):

        self.name = name
        self.phone_no = phone_no
        self.no_of_books = no_of_books
        self.books_taken = books_taken

    def display_books(self):
        for book_name, no_of_books in self.books.items():
            print(f"{book_name}: {no_of_books}")
        print("----------------")

    def display_user(self):
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_no}")
        print(f"Books Taken: {', '.join(self.books_taken) if self.books_taken else 'None'}")
        print(f"Number of Books: {self.no_of_books}")

    def borrow(self):
        if self.no_of_books < len(self.books):
            print(f"Books Taken:{self.books_taken}")
            book_you_want = input("Which book do you want? ")
            if book_you_want not in self.books_taken:
                if self.no_of_books < 4:
                    if book_you_want in self.books:
                        if self.books[book_you_want] > 0:
                            print(f"Quantity is available for {book_you_want}.")

                            self.books[book_you_want] -= 1
                            self.no_of_books += 1
                            self.books_taken.append(book_you_want)

                            print("Borrowed successfully!")
                        else:
                            print(f"Sorry, {book_you_want} is currently unavailable.")
                    else:
                        print(f"{book_you_want} is not present in the library.")
                else:
                    print("You cannot borrow more than four books. Return a book to borrow another.")
            else:
                print(f"You already have {book_you_want}.")

        else:
            print("you already bought all books")

    def return_book(self):
        if self.no_of_books > 0:
            print(f"Number of Books: {self.no_of_books}")
            book_you_return = input("Which book would you like to return? ")
            if book_you_return in self.books_taken:
                print(f"Returning {book_you_return}")

                self.books[book_you_return] += 1
                self.books_taken.remove(book_you_return)
                self.no_of_books -= 1

                print("Returned successfully")
            else:
                print(f"{book_you_return} is not in your borrowed books list.")

        else:
            print("you dont have books to return")

    @staticmethod
    def display(self):
        while True:

            print(f"\n1.Display Books", "\t2.Display User Info", "\t3.Borrow a Book", "\t4.Return a Book", "\t5.Exit")
            n = int(input("Choose an option: "))

            if n == 1:
                self.display_books()
            elif n == 2:
                self.display_user()
            elif n == 3:
                self.borrow()
            elif n == 4:
                self.return_book()
            elif n == 5:

                print("HAPPY LEARNING")
                print("THANK YOU")
                break
            else:
                print("Invalid choice. Please try again.\n")


# Example usage2
student1 = User('robin', 9003343537, 1, ['a'])
student2 = User('inba', 8838710086, 2, ['a', 'b'])
student3 = User('vasi', 9999900000, 1, ['a', 'c'])
student4 = User('yuvi', 999998800, 2, ['a', 'c', ])
student5 = User('selva', 9999921000, 1, ['c'])
student6 = User('vasi', 9999900000, 4, ['a', 'c', 'b', 'd'])

User.display(student1)
#
# User.display(student2)
#
# User.display(student3)
# User.display(student4)
# User.display(student6)
