class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrower = None

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.borrowed_books = []

class UniversityLibrary:
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, book):
        self.books.append(book)

    def add_student(self, student):
        self.students.append(student)

    def display_books(self):
        print("Books in the University Library:")
        for index, book in enumerate(self.books, start=1):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{index}. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")

    def search_books(self, keyword):
        print(f"Search results for '{keyword}':")
        for index, book in enumerate(self.books, start=1):
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"{index}. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")

    def view_students(self):
        print("Students in the University Library:")
        for student in self.students:
            print(f"Student ID: {student.student_id}, Name: {student.name}")

    def borrow_book(self, book_index, student_id):
        if 0 < book_index <= len(self.books):
            book = self.books[book_index - 1]
            student = self.find_student_by_id(student_id)
            if book.is_borrowed:
                print(f"'{book.title}' is already borrowed by {book.borrower.name}.")
            elif student:
                book.is_borrowed = True
                book.borrower = student
                student.borrowed_books.append(book)
                print(f"{student.name} has borrowed '{book.title}'.")
            else:
                print("Student not found.")
        else:
            print("Invalid book index.")

    def return_book(self, book_index):
        if 0 < book_index <= len(self.books):
            book = self.books[book_index - 1]
            if book.is_borrowed:
                student = book.borrower
                book.is_borrowed = False
                book.borrower = None
                student.borrowed_books.remove(book)
                print(f"'{book.title}' has been returned by {student.name}.")
            else:
                print(f"'{book.title}' is not currently borrowed.")
        else:
            print("Invalid book index.")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

def main():
    university_library = UniversityLibrary()

    while True:
        print("University of Benin Library Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Books")
        print("4. View Students")
        print("5. Borrow Book")
        print("6. Return Book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            university_library.add_book(book)
            print("Book added successfully!")

        elif choice == '2':
            university_library.display_books()

        elif choice == '3':
            keyword = input("Enter keyword to search for: ")
            university_library.search_books(keyword)

        elif choice == '4':
            university_library.view_students()

        elif choice == '5':
            university_library.display_books()
            book_index = int(input("Enter the index of the book you want to borrow: "))
            student_id = input("Enter your student ID: ")
            university_library.borrow_book(book_index, student_id)

        elif choice == '6':
            university_library.display_books()
            book_index = int(input("Enter the index of the book you want to return: "))
            university_library.return_book(book_index)

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
