from book import Book
class LibraryBook(Book):
    def __init__(self, title, author, inventory):
        super().__init__(title, author)
        self.inventory = inventory
        self.borrowers = []

    def check_out(self, name):
        if self.inventory < 1:
            print("Sorry, not available.")
        self.inventory -= 1
        self.borrowers.append(name)
        return self

    def show_inventory(self):
        for i in range(len(self.borrowers)):
            print(f"Borrower #{i + 1}: {self.borrowers[i]}")
        print(f"Books Left: {self.inventory}")
        return self

b1 = LibraryBook("Cat in the Hat", "Dr. Suess", 10)
b1.print_info().check_out("John").check_out("Bob").check_out("Josh")
b1.show_inventory()

b2 = LibraryBook("Harry Potter", "J.K. Rowling", 3)
b2.check_out("Susan").check_out("Emily").check_out("Robert").show_inventory()