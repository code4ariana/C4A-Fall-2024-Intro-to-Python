'''
Library Management System
Created By Ariana Walcott


index number or a string
Homework #3
'''


def menu():
    print("----------------------------------------")
    print("Welcome to the Library Management System")
    print("1. Add a book")
    print("2. List available books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")
    print("----------------------------------------")

# book one info

book1_title = "The Great Gatsby"
book1_author = "F.Scott Fitzgerald"
book1_year = 1925
book1_available = True

# book two info

book2_title = "1984"
book2_author = "George Orwell"
book2_year = 1949
book2_available = True

# book three info

book3_title = "To Kill a Mockingbird"
book3_author = "Harper Lee"
book3_year = 1960
book3_available = True

books = ["The Great Gatsby", "1984", "To Kill a Mockingbird"]
available_books = []

def add_books():
    book_choice = input("What book would you like to add to the library?: ")
    for book in books:
        available_books.append(book_choice)
        print("You have added, " +  book_choice)
        print("\n")
        print("**********************")
        return_to_menu = input("Return to the menu?: ")
        if return_to_menu == "Yes":
            menu()
            menu_selection = int(input("Choose an option: "))
            print("Last actions: \n")
        else:
            exit()
            pass
    
def list_books():
    print(books)
    print("\n")
    print("**********************")
    return_to_menu = input("Return to the menu?: ")
    if return_to_menu == "Yes":
        menu()
    else:
        exit()
        pass

def borrow_book():
    for book in books:
            print(book)
    remove_book_from_list = input("What book would you like to borrow from the library?: ")
    if remove_book_from_list == "The Great Gatsby":
            global book1_available
            if book1_available == True:
                books.remove(book1_title)
                print("Confirmed!")
                print(books)
                book1_available = False
    elif book2_title == "George Orwell":
         if book1_available == True:
             availableBooks.remove(book2_title)
             book2_available = False
             print("Confirmed!")
             print(remove_book_from_list + " is no longer available")
    elif book3_title == "To Kill a Mockingbird":
          books.remove(book3_title)
          book3_available = False
          print("Confirmed!")
          print(remove_book_from_list + " is no longer available")
    else:
        print("Entry is no longer available")
        pass

def return_book():
    return_book = input("What book would you like to return to the library\n")
    print("You have returned " + return_book)
    print("\n")
    print("**********************")
    print(menu)
    pass

def end_of_program():
    exit()
    pass


def main():
    menu()
    menu_selection = int(input("Choose an option: "))
    
    if menu_selection == 1:
        add_books()
    elif menu_selection == 2:
        list_books()
    elif menu_selection == 3:
          borrow_book()
    elif menu_selection == 4:
         return_book()
    elif menu_selection == 5:
         end_of_program()
    else:
        print("Entry was not valid")


# call main function
main()
