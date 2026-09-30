import json
import os


# ============================================================
# COLLEGEMATE
# Student Utility Application
# ============================================================


# ============================================================
# VALIDATION FUNCTIONS
# ============================================================

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# ============================================================
# CGPA CALCULATOR
# ============================================================

def calculate_cgpa():

    print("\n===== CGPA CALCULATOR =====")

    subjects = get_integer(
        "Enter total number of subjects: "
    )

    if subjects <= 0:
        print("Number of subjects must be greater than 0.")
        return

    total_points = 0
    total_credits = 0

    for i in range(subjects):

        print("\nSubject", i + 1)

        grade = get_number(
            "Enter grade point (0-10): "
        )

        credit = get_number(
            "Enter credit: "
        )

        if grade < 0 or grade > 10:
            print("Grade point must be between 0 and 10.")
            return

        if credit <= 0:
            print("Credit must be greater than 0.")
            return

        total_points += grade * credit
        total_credits += credit

    cgpa = total_points / total_credits

    print("\nYour CGPA is:", round(cgpa, 2))

    with open("saved_data.txt", "a") as file:
        file.write(
            "CGPA: "
            + str(round(cgpa, 2))
            + "\n"
        )

    print("CGPA saved successfully!")


# ============================================================
# ATTENDANCE CALCULATOR
# ============================================================

def calculate_attendance():

    print("\n===== ATTENDANCE CALCULATOR =====")

    total_classes = get_integer(
        "Enter total classes: "
    )

    attended_classes = get_integer(
        "Enter classes attended: "
    )

    if total_classes <= 0:
        print("Total classes must be greater than 0.")
        return

    if attended_classes < 0:
        print("Attended classes cannot be negative.")
        return

    if attended_classes > total_classes:
        print(
            "Attended classes cannot be greater "
            "than total classes."
        )
        return

    attendance = (
        attended_classes / total_classes
    ) * 100

    print(
        "\nYour attendance is:",
        round(attendance, 2),
        "%"
    )

    if attendance >= 75:
        print("Status: Eligible (75% or above)")
    else:
        print("Status: Below 75%")

    with open("saved_data.txt", "a") as file:
        file.write(
            "Attendance: "
            + str(round(attendance, 2))
            + "%\n"
        )

    print("Attendance saved successfully!")


# ============================================================
# ASSIGNMENT TRACKER
# ============================================================

def load_assignments():

    if not os.path.exists("assignments.json"):
        return []

    try:

        with open("assignments.json", "r") as file:
            return json.load(file)

    except:

        return []


def save_assignments(assignments):

    with open("assignments.json", "w") as file:
        json.dump(
            assignments,
            file,
            indent=4
        )


def show_assignments(assignments):

    if len(assignments) == 0:

        print("\nNo assignments yet.")
        return False

    print("\n===== YOUR ASSIGNMENTS =====")

    for i, assignment in enumerate(
        assignments,
        1
    ):

        print(
            i,
            ".",
            assignment["name"],
            "-",
            assignment["status"]
        )

    return True


def assignment_tracker():

    assignments = load_assignments()

    while True:

        print("\n===== ASSIGNMENT TRACKER =====")

        print("1. Add assignment")
        print("2. View assignments")
        print("3. Mark as completed")
        print("4. Delete assignment")
        print("5. Back")

        choice = input(
            "Enter your choice: "
        )

        # ADD
        if choice == "1":

            name = input(
                "Enter assignment name: "
            ).strip()

            if name == "":
                print(
                    "Assignment name cannot be empty."
                )
                continue

            assignment = {
                "name": name,
                "status": "Pending"
            }

            assignments.append(assignment)

            save_assignments(assignments)

            print(
                "Assignment added successfully!"
            )

        # VIEW
        elif choice == "2":

            show_assignments(assignments)

        # COMPLETE
        elif choice == "3":

            if show_assignments(assignments):

                number = get_integer(
                    "Enter assignment number: "
                )

                if (
                    number < 1
                    or number > len(assignments)
                ):

                    print(
                        "Invalid assignment number."
                    )

                else:

                    assignments[
                        number - 1
                    ]["status"] = "Completed"

                    save_assignments(
                        assignments
                    )

                    print(
                        "Assignment marked as completed!"
                    )

        # DELETE
        elif choice == "4":

            if show_assignments(assignments):

                number = get_integer(
                    "Enter assignment number: "
                )

                if (
                    number < 1
                    or number > len(assignments)
                ):

                    print(
                        "Invalid assignment number."
                    )

                else:

                    deleted = assignments.pop(
                        number - 1
                    )

                    save_assignments(
                        assignments
                    )

                    print(
                        deleted["name"],
                        "deleted successfully!"
                    )

        # BACK
        elif choice == "5":

            break

        else:

            print("Invalid choice.")


# ============================================================
# EXPENSE TRACKER
# ============================================================

def load_expenses():

    if not os.path.exists("expenses.json"):
        return []

    try:

        with open("expenses.json", "r") as file:
            return json.load(file)

    except:

        return []


def save_expenses(expenses):

    with open("expenses.json", "w") as file:
        json.dump(
            expenses,
            file,
            indent=4
        )


def show_expenses(expenses):

    if len(expenses) == 0:

        print("\nNo expenses yet.")
        return False

    print("\n===== YOUR EXPENSES =====")

    total = 0

    for i, expense in enumerate(
        expenses,
        1
    ):

        print(
            i,
            ".",
            expense["name"],
            "- ₹",
            expense["amount"]
        )

        total += expense["amount"]

    print("-------------------------")
    print(
        "Total expense: ₹",
        total
    )

    return True


def expense_tracker():

    expenses = load_expenses()

    while True:

        print("\n===== EXPENSE TRACKER =====")

        print("1. Add expense")
        print("2. View expenses")
        print("3. Delete expense")
        print("4. Back")

        choice = input(
            "Enter your choice: "
        )

        # ADD
        if choice == "1":

            name = input(
                "Enter expense name: "
            ).strip()

            if name == "":
                print(
                    "Expense name cannot be empty."
                )
                continue

            amount = get_number(
                "Enter amount: "
            )

            if amount < 0:

                print(
                    "Amount cannot be negative."
                )

                continue

            expense = {
                "name": name,
                "amount": amount
            }

            expenses.append(expense)

            save_expenses(expenses)

            print(
                "Expense added successfully!"
            )

        # VIEW
        elif choice == "2":

            show_expenses(expenses)

        # DELETE
        elif choice == "3":

            if show_expenses(expenses):

                number = get_integer(
                    "Enter expense number: "
                )

                if (
                    number < 1
                    or number > len(expenses)
                ):

                    print(
                        "Invalid expense number."
                    )

                else:

                    deleted = expenses.pop(
                        number - 1
                    )

                    save_expenses(expenses)

                    print(
                        deleted["name"],
                        "deleted successfully!"
                    )

        # BACK
        elif choice == "4":

            break

        else:

            print("Invalid choice.")


# ============================================================
# SAVED DATA
# ============================================================

def saved_data_menu():

    while True:

        print("\n===== SAVED DATA =====")

        print("1. Save new data")
        print("2. View saved data")
        print("3. Clear saved data")
        print("4. Back")

        choice = input(
            "Enter your choice: "
        )

        # SAVE
        if choice == "1":

            data = input(
                "Enter something to save: "
            ).strip()

            if data == "":
                print(
                    "Data cannot be empty."
                )
                continue

            with open(
                "saved_data.txt",
                "a"
            ) as file:

                file.write(
                    data + "\n"
                )

            print(
                "Data saved successfully!"
            )

        # VIEW
        elif choice == "2":

            if not os.path.exists(
                "saved_data.txt"
            ):

                print(
                    "No saved data yet."
                )

            else:

                with open(
                    "saved_data.txt",
                    "r"
                ) as file:

                    data = file.read()

                if data.strip() == "":

                    print(
                        "No saved data yet."
                    )

                else:

                    print(
                        "\n===== SAVED DATA ====="
                    )

                    print(data)

        # CLEAR
        elif choice == "3":

            confirm = input(
                "Are you sure? "
                "Type yes to confirm: "
            ).lower()

            if confirm == "yes":

                with open(
                    "saved_data.txt",
                    "w"
                ) as file:

                    file.write("")

                print(
                    "Saved data cleared!"
                )

            else:

                print(
                    "Saved data was not cleared."
                )

        # BACK
        elif choice == "4":

            break

        else:

            print("Invalid choice.")


# ============================================================
# MAIN MENU
# ============================================================

def show_menu():

    print("\n")
    print("=" * 45)
    print("              COLLEGEMATE")
    print("          Your Student Utility")
    print("=" * 45)

    print("1. CGPA Calculator")
    print("2. Attendance Calculator")
    print("3. Assignment Tracker")
    print("4. Expense Tracker")
    print("5. Saved Data")
    print("6. Exit")

    print("=" * 45)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            calculate_cgpa()

        elif choice == "2":

            calculate_attendance()

        elif choice == "3":

            assignment_tracker()

        elif choice == "4":

            expense_tracker()

        elif choice == "5":

            saved_data_menu()

        elif choice == "6":

            print(
                "\nThank you for using CollegeMate!"
            )

            break

        else:

            print(
                "Invalid choice. "
                "Please enter 1-6."
            )


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":

    main()