import csv
import os
from datetime import datetime


# Function to display menu options
def display_menu():
    print("Expense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Monthly Summary")
    print("3. View Category-wise Expenditure")
    print("4. Exit")


# Function to add expense
def add_expense():
    amount = float(input("Enter expense amount: "))
    description = input("Enter expense description: ")
    category = input("Enter expense category: ")
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, description, category])
    print("Expense added successfully!")


# Function to view monthly summary
def view_monthly_summary():
    month = input("Enter month (MM/YYYY): ")
    total_amount = 0
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].startswith(month):
                total_amount += float(row[1])
    print(f"Total expenses for {month}: ${total_amount:.2f}")


# Function to view category-wise expenditure
def view_category_wise_expenditure():
    category = input("Enter category: ")
    total_amount = 0
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3].lower() == category.lower():
                total_amount += float(row[1])
    print(f"Total expenses for {category}: ${total_amount:.2f}")


# Main function
def main():
    if not os.path.exists('expenses.csv'):
        with open('expenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Amount', 'Description', 'Category'])

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_monthly_summary()
        elif choice == '3':
            view_category_wise_expenditure()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()
