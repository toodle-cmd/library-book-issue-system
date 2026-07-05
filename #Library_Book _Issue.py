#Library Book Issue
from datetime import datetime ,timedelta
today=datetime.now()
date=today.strftime("%d/%m/%Y")   
new_date = today + timedelta(days=10)

print(date)
print("\n Library Book Issue System  ")
print("\n")

Student_Name=input("\nenter your name:")
Student_ID=(input("\nenter your student_id {roll_no}:"))
if Student_ID.count("/") == 1:
    print()
else:
    print(f"INVALID Student_ID : {Student_ID}")
    exit()



books = {
    "Pride and Prejudice": "Jane Austen",
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "Harry Potter and the Philosopher's Stone": "J. K. Rowling",
    "The Alchemist": "Paulo Coelho",
    "The Hobbit": "J. R. R. Tolkien",
    "The Da Vinci Code": "Dan Brown",
    "The Catcher in the Rye": "J. D. Salinger",
    "Wings of Fire": "A. P. J. Abdul Kalam"
}
print("\n Available Books ")
for book ,author in books.items():
    print(f"{book}-->{author}")
author_name=input("\nEnter author_name:")
author_book=input("\nEnter book_name:")

if author_book in books and books[author_book] == author_name:
    print("\nYes, this book is available")
    print(f"{date}: {Student_Name} ({Student_ID}) has issued the book '{author_book}'.")
    print("\nReturn date:", new_date.strftime("%d/%m/%Y"))
elif author_book not in books:
    print("\n Book Not Available")
else:
    print("\nAuthor and book do not match.")




print("\n ")
print("\nGuidelines for Issuing Books from the Library:")
print("\nStudents must carry their library card while issuing books.," \
"\nBooks should be issued only in the student's name.," \
"\nStudents must check the condition of the book before borrowing it.," \
"\nThe due date should be noted carefully.," \
"\nBooks must be returned on or before the due date.," \
"\nLate returns may result in a fine.," \
"\nLost or damaged books must be replaced or paid for by the student.," \
"\nLibrary books should be handled with care and kept clean.," \
"\nBorrowed books should not be transferred to another student." \
"\nStudents must follow all library rules and maintain discipline in the library.")
print("\n\nThank you for issuing a book from the library.")

print("\n\nBOOK REISSUE")

Reissue_date = input("enter yes or no :").lower()

if Reissue_date == "yes":
    update_date=new_date + timedelta(days=10)
    print(f"New return date: {update_date.strftime('%d/%m/%Y')}")
    print("\n\nThank you for issuing a book from the library.")
else:
    exit()



