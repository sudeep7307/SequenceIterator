import sys

class Book:
    def __init__(self, title, author, year, file):
        self.title = title
        self.author = author
        self.year = year
        self.file = file

    def __repr__(self):
        return f"{self.title} by {self.author}"
    
class EBookReader:
    def __init__(self):
        self.books = [
            Book("The Adventures of Sherlock Holmes", "Sir Arthur Conan Doyle", 1892, "sherlock_holmes.txt"),
            Book("Pride and Prejudice", "Jane Austen", 1813, "pride_prejudice.txt"),
            Book("I Feel Bad About My Neck", "Nora Ephron", 2006, "IFeelBadAboutMyNeck.txt"),
            Book("Harry Potter and the Goblet of Fire", 2000, "JK Rowling", "HarryPotter.txt")
        ]
        self.purchased_books = []

    def buy_book(self, title):
        book = next((b for b in self.books if b.title == title), None)
        if book:
            self.purchased_books.append(book)
            print(f"You bought {title}!")
        else:
            print("sorry, we don't have that book available.")

    def view_books(self):
        print("Your purchased books:")
        for idx, book in enumerate(self.purchased_books):
            print(f"{idx + 1}. {book}")
    
    def read_book(self, title):
        book = next((b for b in self.purchased_books if b.title == title), None)
        if book:
            print("Here's your book:")
            with open(book.file, "r") as f:
                print(f.read())
        else:
            print("Sorry, you don't have that book.")

def main():
    reader = EBookReader()

    while True:
        print("\nOptions:")
        print("1. Buy a book")
        print("2. View purchased books")
        print("3. Read a book")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == "1":
            title = input("Enter the title of the book: ")
            reader.buy_book(title)
        elif choice == "2":
            reader.view_books()
        elif choice == "3":
            title = input("Enter the title of the book: ")
            reader.read_book(title)
        elif choice == "4":
            sys.exit(0)
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()