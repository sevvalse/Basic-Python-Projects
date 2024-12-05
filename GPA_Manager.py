import sqlite3 as sql


# Function to connect to the SQLite database
def connect_db():
    # Replace the path with the correct location of your database file
    return sql.connect('users.db')


# Function to add a new user to the database
def add_user(cur, username, password):
    try:
        # Insert a new user into the 'mathgrades' table
        cur.execute("INSERT INTO mathgrades (usernames, passwords) VALUES (?, ?)", (username, password))
        print(f"User '{username}' has been added!")  # Confirmation message
    except sql.IntegrityError:
        # Handle the case where the username already exists
        print(f"User '{username}' already exists!")


# Function to authenticate a user based on username and password
def authenticate_user(cur, username, password):
    # Query the database for the password associated with the given username
    cur.execute("SELECT passwords FROM mathgrades WHERE usernames = ?", (username,))
    result = cur.fetchone()
    # Return True if the password matches, otherwise False
    return result and result[0] == password


# Function to update grades (midterm or final) for a specific user
def update_grade(cur, user, grade_type, grade):
    # Update the specified grade for the given user
    cur.execute(f"UPDATE mathgrades SET {grade_type} = ? WHERE usernames = ?", (grade, user))
    print(f"{grade_type.capitalize()} grade '{grade}' has been added!")


# Function to view grades for a specific user
def view_grades(cur, user):
    grades = {}
    # Query the database for both midterm and final grades
    for grade_type in ["midterms", "finals"]:
        cur.execute(f"SELECT {grade_type} FROM mathgrades WHERE usernames = ?", (user,))
        # Store the result or a message indicating no grade available
        grades[grade_type] = cur.fetchone()[0] or "No grade available"
    return grades


# Function to calculate GPA from midterm and final grades
def calculate_gpa(midterm, final):
    return midterm * 0.4 + final * 0.6


def main():
    # Connect to the database and create a cursor
    con = connect_db()
    cur = con.cursor()

    # Main loop for menu options
    while True:
        choice = input("\nWelcome! Please select an option:\n1 - Select a user\n2 - Add a user\n3 - Exit\n")

        if choice == '1':  # Option to log in as an existing user
            user = input("Enter username: ")
            password = input("Enter password: ")

            if authenticate_user(cur, user, password):  # Check if username and password match
                print("Login successful!")
                while True:
                    action = input("\n1 - Add grades\n2 - View grades\n3 - Exit\n")

                    if action == '1':  # Option to add grades
                        grade_type = input("1 - Midterm\n2 - Final\n")
                        grade = input("Enter grade: ")
                        # Update the appropriate grade type
                        update_grade(cur, user, "midterms" if grade_type == '1' else "finals", grade)
                        con.commit()
                    elif action == '2':  # Option to view grades
                        grades = view_grades(cur, user)
                        # Convert grades to float for GPA calculation, defaulting to 0 if not found
                        midterm = float(grades.get("midterms", 0))
                        final = float(grades.get("finals", 0))
                        gpa = calculate_gpa(midterm, final)
                        print(f"Grades: {grades}\nGPA: {gpa:.2f}")
                    elif action == '3':  # Exit the user-specific menu
                        break
                    else:
                        print("Invalid selection.")
            else:
                print("Incorrect username or password.")
        elif choice == '2':  # Option to add a new user
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            add_user(cur, username, password)
            con.commit()  # Commit the new user to the database
        elif choice == '3':  # Exit the program
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

    con.close()  # Close the database connection
