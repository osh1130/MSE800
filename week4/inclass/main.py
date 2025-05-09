from database import create_table
from user_manager import add_user, advanced_search, view_users, search_user, delete_user
from course_manager import insert_course, search_course_by_id_and_userid

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Search User by Name and ID")
    print("7. Insert Course")
    print("8. Search Course by Course ID and User Name")


def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-8): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
            break
        elif choice == '6':
            try:
                user_id = int(input("Enter user ID: "))
            except ValueError:
                print("Invalid ID. Please enter a number.")
                continue
            name = input("Enter name to search: ")
            users = advanced_search(user_id, name)
            if users:
                for user in users:
                    print(user)
            else:
                print("No matching user found.")
        elif choice == '7':
            course_name = input("Enter course name: ")
            unit = int(input("Enter course unit: "))
            user_id = int(input("Enter user ID to assign this course to: "))
            insert_course(course_name, unit, user_id)


        elif choice == '8':
            course_id = input("Enter course ID: ")
            user_id = input("Enter user ID: ")
            courses = search_course_by_id_and_userid(course_id, user_id)
            if courses:
                for course in courses:
                    print(course)
            else:
                print("No matching course found.")

        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
