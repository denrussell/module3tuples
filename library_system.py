'''
2. Python Data Structure Challenges in Real-World Scenarios
Task 1: Library System Enhancement 
Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where each book is stored as a tuple 
within a list. Your task is to update this system by adding new books and ensuring no 
duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is
 handled appropriately.

'''

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# I need to def a function to add to the list:

def add_book(library):
    book = input("Enter title of the book: ")
    author = input("Enter author of the book: ")
    new_book = (book, author)
    library.append(new_book) 
    
    if new_book not in library:
        print (f"New book '{new_book}' has been added") 
    else:
        print(f"{new_book} already exists.")
    
    print(library)

add_book(library)
