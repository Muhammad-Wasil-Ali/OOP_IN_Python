import pdb
class Book:
    def __init__(self, title, author, isbn, isAvailable=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isAvailable = isAvailable
    
    def checkoutBook(self):
        if self.isAvailable:
            self.isAvailable = False
            print(f"Book '{self.title}' checked out successfully")
        else:
            print(f"Book '{self.title}' is already checked out")
            
    def returnBook(self):
        if not self.isAvailable:
            self.isAvailable = True
            print(f"Book '{self.title}' returned successfully")
        else:
            print(f"Book '{self.title}' was not checked out")
    
    def __str__(self):
        status = "Available" if self.isAvailable else "Checked out"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"


class Library:
    def __init__(self):
        self.allBooks = []  # Instance variable, not class variable
         
    def addBook(self, book):
        self.allBooks.append(book)
        print(f"Book '{book.title}' added to library")
        
    def removeBook(self, isbn):
        for book in self.allBooks:
            if book.isbn == isbn:
                self.allBooks.remove(book)  # Fixed typo
                print(f"Book with ISBN {isbn} removed")
                return
        print(f"Book with ISBN {isbn} not found")

    def searchByTitle(self, title):
        found_books = []
        for book in self.allBooks:
            if book.title.lower() == title.lower():
                found_books.append(book)
        
        if found_books:
            print(f"\nFound {len(found_books)} book(s) with title '{title}':")
            for book in found_books:
                print(book)
        else:
            print(f"No books found with title '{title}'")
        return found_books
            
    def searchByAuthor(self, author):  # Fixed typo in method name
        found_books = []
        for book in self.allBooks:
            if book.author.lower() == author.lower():  # Added ()
                found_books.append(book)
        
        if found_books:
            print(f"\nFound {len(found_books)} book(s) by '{author}':")
            for book in found_books:
                print(book)
        else:
            print(f"No books found by author '{author}'")
        return found_books
    
    def checkOutBook(self, isbn):
        for book in self.allBooks:
            if book.isbn == isbn:
                book.checkoutBook()
                return
        print(f"Book with ISBN {isbn} not found")
    
    def returnBookToLibrary(self, isbn):
        for book in self.allBooks:
            if book.isbn == isbn:
                book.returnBook()
                return
        print(f"Book with ISBN {isbn} not found")
    
    def displayAllBooks(self):
        if not self.allBooks:
            print("Library is empty")
            return
        print(f"\n=== All Books in Library ({len(self.allBooks)} total) ===")
        for book in self.allBooks:
            print(book)


# Test the code
book1 = Book("Devops", "wasil", "12345", True)
book2 = Book("PDA", "wasil", "54321", False)
book3 = Book("HC", "wasil", "34512", True)
print(book3)
pdb.set_trace()
library = Library()

library.addBook(book1)
library.addBook(book2)
library.addBook(book3)

print("\n--- Testing Search ---")
library.searchByTitle("Devops")
library.searchByAuthor("wasil")

print("\n--- Testing Checkout/Return ---")
library.checkOutBook("12345")
library.returnBookToLibrary("12345")

print("\n--- Display All Books ---")
library.displayAllBooks()