# Library Book Manager
# This program lets users add and view books in a small library using classes.

# Define a Book class to store book title and author
class Book:
    def __init__(self, title, author):
        # Initialize a book with a title and an author
        self.title = title
        self.author = author

    def __str__(self):
        # Return a string in the format "Title by Author"
        return f"{self.title} by {self.author}"

# Define a Library class to manage a list of books
class Library:
    def __init__(self):
        # Initialize an empty list to store book objects
        self.books = []

    def add_book(self, title, author):
        # Create a Book object and add it to the list
        book = Book(title, author)
        self.books.append(book)
        print(f'"{title}" has been added to the library.\n')

    def show_books(self):
        # Display all books currently in the library
        if not self.books:
            print("No books in the library.\n")
        else:
            print("Books in the library:")
            for book in self.books:
                print("- " + str(book))
            print()  # Extra newline for spacing

# Main program to interact with the library
def main():
    library = Library()

    while True:
        # Display menu
        print("========== Library Menu ==========")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Exit")
        print("==================================")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            # Add a book
            print("\n-- Add a New Book --")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            # Show all books
            print("\n-- List of Books --")
            library.show_books()
        elif choice == '3':
            # Exit the program
            print("Goodbye! Exiting the program.")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please enter 1, 2, or 3.\n")

# Start the program
if __name__ == "__main__":
    main()
