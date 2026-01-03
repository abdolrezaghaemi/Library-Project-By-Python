import json
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#reading json
with open("admins.json", "r", encoding="utf-8") as f:
    admins_json_data = json.load(f)

with open("librarians.json", "r", encoding="utf-8") as f:
    librarians_json_data = json.load(f)

with open("users.json", "r", encoding="utf-8") as f:
    users_json_data = json.load(f)

with open("books.json", "r", encoding="utf-8") as f:
    books_json_data = json.load(f)

with open("loans.json", "r", encoding="utf-8") as f:
    loans_json_data = json.load(f)


json_mapping = {
    "admins_data": ("admins.json", "Admins"),
    "librarian_data": ("librarians.json", "Librarian"),
    "users_data": ("users.json", "Users"),
    "books_data": ("books.json", "Books"),
    "loans_data": ("loans.json", "loans"),
}

def save_data(data_var_name, data_list):
    if data_var_name in json_mapping:
        filename, key = json_mapping[data_var_name]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({key: data_list}, f, ensure_ascii=False, indent=4)
        print(f"Data saved successfully to {filename}")
    else:
        print(f"No JSON mapping found for variable '{data_var_name}'")


#editing json
with open("admins.json", "w", encoding="utf-8") as f:
    json.dump(admins_json_data, f, ensure_ascii=False, indent=4)

with open("librarians.json", "w", encoding="utf-8") as f:
    json.dump(librarians_json_data, f, ensure_ascii=False, indent=4)

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(users_json_data, f, ensure_ascii=False, indent=4)

with open("books.json", "w", encoding="utf-8") as f:
    json.dump(books_json_data, f, ensure_ascii=False, indent=4)

with open("user_loans.json", "w", encoding="utf-8") as f:
    json.dump(loans_json_data, f, ensure_ascii=False, indent=4)



admins_data = admins_json_data["Admins"]
librarian_data = librarians_json_data["Librarian"]
users_data = users_json_data["Users"]
books_data = books_json_data["Books"]
loans_data = loans_json_data["loans"]

current_admin_name = None
current_librarian_name = None
current_user_name = None
current_admin_username = None
current_librarian_username = None
current_user_username = None


#functions of role
def get_role():
    while True:
        clear_screen()
        print("Welcome to the Library Management System")
        print("1. Admin")
        print("2. Librarian")
        print("3. User")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            return gate_admins()
        elif choice == "2":
            return gate_librarian()
        elif choice == "3":
            return gate_users()
        elif choice == "0":
            print("Goodbye")
            sys.exit()
        else:
            print("Invalid choice")
            input("Press Enter to try again...")


#functions of gates
def gate_admins():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for admin in admins_data:
            if admin["username"] == username and admin["password"] == password:
                clear_screen() 
                return admins_panel(admin["name"])

        else:
            print("Invalid username or password")
            if input("Do you want to try again? (yes/no): ").lower() == "yes": 
                clear_screen()
                return gate_admins()
            
            else:
                clear_screen()
                return get_role()

        

def gate_librarian():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for librarian in librarian_data:
        if librarian["username"] == username and librarian["password"] == password and librarian["status"] == "active":
            clear_screen()        
            return librarian_panel(librarian["name"])
            
    else:
        print("Invalid username or password or librarian is not active")
        if input("Do you want to try again? (yes/no): ").lower() == "yes": 
            clear_screen()
            return gate_librarian()
        else:
            clear_screen()
            return get_role()


def gate_users():
    global current_user_name
    global current_user_username
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in users_data:
        if user["username"] == username and user["password"] == password and user["status"] == "active":
            current_user_name = user["name"]
            current_user_username = user["username"]
            clear_screen()
            return users_panel(current_user_name, current_user_username)
    else:
        print("Invalid username or password or user is not active")
        if input("Do you want to try again? (yes/no): ").lower() == "yes": 
            clear_screen()
            return gate_users()
        else:
            clear_screen()
            return get_role()


#functions of panels
def admins_panel(name):
    while True:
        clear_screen()
        print(f"Welcome {name} to your panel")
        print("1. signing up a new user")
        print("2. signing up a new librarian")
        print("3. removing or disabaling users")
        print("4. removing or disabaling librarians")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            signing_up_a_new_user()
        elif choice == "2":
            signing_up_a_new_librarian()
        elif choice == "3":
            removing_or_disabaling_users()
        elif choice == "4":
            removing_or_disabaling_librarians()
        elif choice == "0":
            print("Goodbye")
            return get_role()
        else:
            print("Invalid choice")


def librarian_panel(name):
    while True:
        clear_screen() 
        print(f"Welcome {name} to your panel")
        print("1. List of requests for books")
        print("2. List of requests for deadline extension")
        print("3. Add new books")
        print("4. Edit books details")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            requests_response_for_books()
        elif choice == "2":
            list_of_requests_for_deadline_extension()
        elif choice == "3":
            add_new_books()
        elif choice == "4":
            edit_books_details()
        elif choice == "0":
            print("Goodbye")
            return get_role()
        else:
            print("Invalid choice")

def users_panel(current_user_name, current_user_username):
    while True:
        clear_screen()
        print(f"Welcome {current_user_name} to your panel")
        print("1. Search for a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. List of borrowed books by you")
        print("5. Request for book deadline extension")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            search_book()
        elif choice == "2":
            borrow_book_from_user(current_user_username)
        elif choice == "3":
            return_book(current_user_username)
        elif choice == "4":
            list_borrowed_books_by_user(current_user_username)
        elif choice == "5":
            request_deadline_extension(current_user_username)
        elif choice == "0":
            print("Goodbye")
            return get_role()
        else:
            print("Invalid choice")


 #functions of actions of admins
def signing_up_a_new_user():
    username = input("Enter the username of the new user: ")
    for user in users_data:
        if user["username"] == username:
            print("Username already exists")
            if input("Do you want to try again? (yes/no): ").lower() == "yes":
                clear_screen() 
                return signing_up_a_new_user()
            else:
                clear_screen()
                return
        else:
            pass
    password = input("Enter the password of the new user: ")
    name = input("Enter the name of the new user: ")
    status = input("Enter the status of the new user(active/disabled): ")
    new_user = {
        "username": username,
        "password": password,
        "name": name,
        "status": status
    }
    users_data.append(new_user)
    save_data("users_data", users_data)
    print("New user signed up successfully")
    input("Press Enter to continue...")
    clear_screen()
    return


def signing_up_a_new_librarian():
    username = input("Enter the username of the new librarian: ")
    for librarian in librarian_data:
        if librarian["username"] == username:
            print("Username already exists")
            if input("Do you want to try again? (yes/no): ").lower() == "yes":
                clear_screen()
                return signing_up_a_new_librarian()
            else:
                clear_screen()
                return
        else:
            pass
    password = input("Enter the password of the new librarian: ")
    name = input("Enter the name of the new librarian: ")
    status = input("Enter the status of the new librarian(active/disabled): ")
    new_librarian = {
        "username": username,
        "password": password,
        "name": name,
        "status": status
    }
    librarian_data.append(new_librarian)
    print("New librarian signed up successfully")
    save_data("librarian_data", librarian_data)
    input("Press Enter to continue...")
    clear_screen()
    return

def removing_or_disabaling_users():
    username = input("Enter the username of the user you want to change status: ")
    for user in users_data:
        if user["username"] == username:
            if user["status"] == "disabled":
                ask1 = input("Do you want to remove or enable this user? (remove/enable): ").lower()
                if ask1 == "remove":
                    users_data.remove(user)
                    print("User removed successfully")
                    save_data("users_data", users_data)
                    input("Press Enter to continue...")
                    clear_screen()
                    return
                elif ask1 == "enable":
                    user["status"] = "active"
                    print("User enabled successfully")
                    save_data("users_data", users_data)
                    input("Press Enter to continue...")
                    clear_screen()
                return
            else:
                ask2 = input("Do you want to remove or disable this user? (remove/disable): ").lower()
                if ask2 == "remove":
                    users_data.remove(user)
                    print("User removed successfully")
                    save_data("users_data", users_data)
                    input("Press Enter to continue...")
                    clear_screen()
                    return
                elif ask2 == "disable":
                    user["status"] = "disabled"
                    print("User disabled successfully")
                    save_data("users_data", users_data)
                    input("Press Enter to continue...")
                    clear_screen()
                    return
    else:
        print("User not found")
        input("Press Enter to continue...")
        clear_screen()
        return
    
def removing_or_disabaling_librarians():
    username = input("Enter the username of the librarian you want change status: ")
    for librarian in librarian_data:
        if librarian["username"] == username:
            if librarian["status"] == "disabled":
                ask1 = input("Do you want to remove or enable this librarian? (remove/enable): ").lower()
                if ask1 == "remove":
                    librarian_data.remove(librarian)
                    print("librarian removed successfully")
                    save_data("librarian_data", librarian_data)
                    input("Press Enter to continue...")
                    clear_screen()
                    return
                elif ask1 == "enable":
                    librarian["status"] = "active"
                    print("librarian enabled successfully")
                    save_data("librarian_data", librarian_data)
                    input("Press Enter to continue...")
                    clear_screen()
                return
            else:
                ask2 = input("Do you want to remove or disable this librarian? (remove/disable): ").lower()
                if ask2 == "remove":
                    librarian_data.remove(librarian)
                    print("librarian removed successfully")
                    save_data("librarian_data", librarian_data)
                    input("Press Enter to continue...")
                    clear_screen()
                    return
                elif ask2 == "disable":
                    librarian["status"] = "disabled"
                    print("librarian disabled successfully")
                    save_data("librarian_data", librarian_data)
                    input("Press Enter to continue...")
                    clear_screen()
                    return
    else:
        print("librarian not found")
        input("Press Enter to continue...")
        clear_screen()
        return
    
 # functions of actions of librarians
requests_for_books_list = []
def book_request_list(title, deadline, current_user_username):
    for book in books_data:
        if book["title"] == title:
            request_b = {
                "pk": len(requests_for_books_list) + 1,
                "user": current_user_username,
                "title": title,
                "deadline": deadline,
                "number": book["number"]
            }
            requests_for_books_list.append(request_b)
            break

def requests_response_for_books():
    if not requests_for_books_list: 
        print("No requests for books")
        input("Press Enter to continue...")
        clear_screen()
        return
    
    print("List of requests for books")
    for request in requests_for_books_list:
        print(f"{request['pk']}: {request['title']} by {request['user']} - Deadline: {request['deadline']} - Number: {request['number']}")
    
    # Accept requests
    response_accept = input("Which request do you want to accept? (enter the request row, comma-separated): ")
    if response_accept:
        response_accept = response_accept.split(",")
        for response in response_accept:
            for request in requests_for_books_list:
                if request["pk"] == int(response):
                    for book in books_data:
                        if book["title"] == request["title"]:
                            book["number"] = int(book["number"]) - 1
                            save_data("books_data", books_data)
                    loan = {
                        "user": request["user"],
                        "title": request["title"],
                        "deadline": request["deadline"]
                    }
                    loans_data.append(loan)
                    save_data("loans_data", loans_data)
                    requests_for_books_list.remove(request)
                    print("Request accepted successfully")
                    break
    
    # Reject requests
    response_reject = input("Which request do you want to reject? (enter the request row, comma-separated): ")
    if response_reject:
        response_reject = response_reject.split(",")
        requests_for_books_list[:] = [req for req in requests_for_books_list if str(req["pk"]) not in response_reject]

    print("Requests processed successfully")
    input("Press Enter to continue...")
    clear_screen()
    return




requests_for_deadline_extension_list = []
def deadline_extension_request_list(title, current_deadline, new_deadline, current_user_username):
    for book in books_data:
        if book["title"] == title:
            for loan in loans_data:
                if loan["user"] == current_user_username and loan["title"] == title:
                    request_e = {
                        "user": current_user_username,
                        "title": title,
                        "new_deadline": new_deadline,
                        "current_deadline": current_deadline
                    }
                    requests_for_deadline_extension_list.append(request_e)
                
            break
def list_of_requests_for_deadline_extension():
    if not requests_for_deadline_extension_list:
        print("No requests for deadline extension")
        input("Press Enter to continue...")
        clear_screen()
        return

    print("List of requests for deadline extension")

    for request_e in requests_for_deadline_extension_list[:]:
        print(
            f"{request_e['title']} by {request_e['user']} - "
            f"Requested Deadline: {request_e['new_deadline']} - "
            f"Current Deadline: {request_e['current_deadline']}"
        )

        response = input("Enter your response (yes/no): ").lower()

        if response == "yes":
            for loan in loans_data:
                if loan["user"] == request_e["user"] and loan["title"] == request_e["title"]:
                    loan["deadline"] = request_e["new_deadline"]
                    save_data("loans_data", loans_data)
            print("Request processed.")
        else:
            print("Request rejected.")


    print("All deadline extension requests processed.")
    input("Press Enter to continue...")
    clear_screen()
def add_new_books():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    number = int(input("Enter the number of copies of the book: "))
    book = {"title": title, "author": author, "number": number}
    books_data.append(book)
    print(f"Book {title} added successfully")
    save_data("books_data", books_data)
    print("Book added successfully")
    input("Press Enter to continue...")
    clear_screen()
    return


def edit_books_details():
    title = input("Enter the title of the book: ")

    book = None
    for b in books_data:
        if b["title"] == title:
            book = b
            break

    if not book:
        print("Book not found")
        input("Press Enter to continue...")
        clear_screen()
        return

    print(f"Book details: {book['title']} by {book['author']} - number: {book['number']}")

    edited = False

    if input("Do you want to edit the book title? (yes/no): ").lower() == "yes":
        book["title"] = input("Enter the new title of the book: ")
        edited = True

    if input("Do you want to edit the book author? (yes/no): ").lower() == "yes":
        book["author"] = input("Enter the new author of the book: ")
        edited = True

    if input("Do you want to edit the number? (yes/no): ").lower() == "yes":
        book["number"] = int(input("Enter the new number: "))
        edited = True

    if edited:
        save_data("books_data", books_data)
        print("Book details edited successfully")
    else:
        print("Book details not edited")

    input("Press Enter to continue...")
    clear_screen()

 # functions of actions of users
def search_book():
    title = input("Enter the title of the book: ")
    for book in books_data:
        if book["title"] == title:
            print(f"{book['title']} by {book['author']} - number: {book['number']}")
            if int(book["number"]) > 0:
                print("This book is available")
                answer_borrow = input("Do you want to borrow this book? (yes/no): ").lower()
                if answer_borrow == "yes":
                    borrow_book_from_search(title)
                    return
                else:
                    answer_ask1 = input("Do you want to try again? (yes/no): ").lower()
                    if answer_ask1 == "yes":
                        search_book()
                        clear_screen()
                        return
                    else:
                        return
            else:
                print("Not available")
                answer_ask2 = input("Do you want to try again? (yes/no): ").lower()
                if answer_ask2 == "yes":
                    search_book()
                    clear_screen() 
                    return
                elif answer_ask2 == "no":
                    clear_screen()
                    return
    else:
        print("Book not found")
        if input("Do you want to try again? (yes/no): ").lower() == "yes":
            search_book()
            return
        else:
            users_panel(current_user_name, current_user_username)
            clear_screen()



def borrow_book_from_search(title):
    global current_user_username
    deadline = input("Enter the deadline: ")
    for book in books_data:
        if book["title"] == title:
            book_request_list(title, deadline, current_user_username)
            print("for knowing the response of the librarian please chack your borrowed list.\nbe paetient, our coworkers are working on it.\n(it will take maximum 24 hours to get the response)")
            input("press enter to continue...")
            clear_screen()
            return                        
    return
def borrow_book_from_user(current_user_username):
    title = input("Enter the title of the book: ")
    for book in books_data:
        if title in book["title"]:
            if int(book["number"]) > 0:
                deadline = input("Enter the deadline: ")
                print("for knowing the response of the librarian please chack your borrowed list.\nbe paetient, our coworkers are working on it.\n(it will take maximum 24 hours to get the response)")
                book_request_list(title, deadline, current_user_username)
                input("press enter to continue...")
                clear_screen()
                return
            else:
                print("Not available")
                print(f"Nearest Deadline Time: {book[min("deadline")]}")
                answer_ask2 = input("Do you want to try again? (yes/no): ").lower()
                if answer_ask2 == "yes":
                    borrow_book_from_user(current_user_username)
                elif answer_ask2 == "no":
                    clear_screen()
                return
    else:
        print("Book not found")
        if input("Do you want to try again? (yes/no): ").lower() == "yes":
            borrow_book_from_user(current_user_username)
        else:
            users_panel(current_user_name, current_user_username)
            clear_screen()


def return_book(current_user_username):
    title = input("Enter the title of the book: ")

    # پیدا کردن کتاب
    book = None
    for b in books_data:
        if b["title"] == title:
            book = b
            break

    if not book:
        print("Book not found")
        input("Press Enter to continue...")
        clear_screen()
        return

    # پیدا کردن loan مربوط به کاربر
    loan = None
    for l in loans_data:
        if l["user"] == current_user_username and l["title"] == title:
            loan = l
            break

    if not loan:
        print("You have not borrowed this book")
        input("Press Enter to continue...")
        clear_screen()
        return

    # بازگرداندن کتاب
    loans_data.remove(loan)
    book["number"] = int(book["number"]) + 1
    save_data("loans_data", loans_data)
    save_data("books_data", books_data)

    print("Book returned successfully")
    input("Press Enter to continue...")
    clear_screen()

def list_borrowed_books_by_user(current_user_username):
    has_books = False

    for loan in loans_data:
        if loan["user"] == current_user_username:
            for book in books_data:
                if book["title"] == loan["title"]:
                    print(f"{book['title']} by {book['author']} - deadline: {loan['deadline']}")
                    has_books = True
    input("Press Enter to continue...")
    clear_screen()

    if not has_books:
        print("You have no borrowed books")
        input("Press Enter to continue...")
        clear_screen()

def request_deadline_extension(current_user_username):
    title = input("Enter the title of the book: ")

    # پیدا کردن کتاب
    book = None
    for b in books_data:
        if b["title"] == title:
            book = b
            break

    if not book:
        print("Book not found")
        input("Press Enter to continue...")
        clear_screen()
        return

    # پیدا کردن loan مربوط به کاربر
    loan = None
    for l in loans_data:
        if l["user"] == current_user_username and l["title"] == title:
            loan = l
            break

    if not loan:
        print("This book is not borrowed by you")
        input("Press Enter to continue...")
        clear_screen()
        return

    # ثبت درخواست تمدید
    new_deadline = input("Enter the new deadline: ")
    current_deadline = loan["deadline"]

    deadline_extension_request_list(
        title,
        current_deadline,
        new_deadline,
        current_user_username
    )

    print(
        "For knowing the response of the librarian please check your borrowed list.\n"
        "Be patient, our coworkers are working on it.\n"
        "(It will take maximum 24 hours to get the response)"
    )

    input("Press Enter to continue...")
    clear_screen()      

get_role()