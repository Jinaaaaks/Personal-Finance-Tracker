import json  # Importing the JSON module to handle saving and loading data
from datetime import datetime  # Importing the datetime module to work with dates
import matplotlib.pyplot as plt  # Importing matplotlib to create visualizations

# Initialize an empty list to store all the transactions
transactions = []

# Initialize an empty list to store all the financial goals
goals = []

def add_transaction(amount, date, description, type):
    '''This function adds a transaction to the transactions list.'''
    # Create a dictionary to store details of the transaction
    transaction = {
        'amount': amount,  # The amount of money involved in the transaction
        'date': date,  # The date when the transaction occurred
        'description': description,  # A short description of the transaction
        'type': type  # The type of transaction: "income" or "expense"
    }
    # Add the transaction dictionary to the transactions list
    transactions.append(transaction)
    # Print a message confirming the transaction was added
    print(f"{type.capitalize()} of {amount} on {date} added: {description}")

def view_transactions():
    '''This function displays all the transactions stored in the transactions list.'''
    # Check if there are any transactions in the list
    if transactions:
        # If there are transactions, loop through each one and print its details
        for transaction in transactions:
            print(f"{transaction['type'].capitalize()} : {transaction['amount']} on {transaction['date']} - {transaction['description']}")
    else:
        # If there are no transactions, print a message saying so
        print("No Transactions Found.")

def calculate_balance():
    '''This function calculates and displays the current balance.'''
    balance = 0  # Initialize balance to 0
    # Loop through each transaction in the transactions list
    for transaction in transactions:
        # If the transaction type is income, add the amount to the balance
        if transaction['type'] == "income":
            balance += transaction['amount']
        # If the transaction type is expense, subtract the amount from the balance
        elif transaction['type'] == "expense":
            balance -= transaction['amount']
    # Print the current balance
    print(f"Current Balance: {balance}")

def set_goal(amount, description, target_date):
    '''This function sets a financial goal.'''
    # Create a dictionary to store details of the goal
    goal = {
        "amount": amount,  # The total amount needed for the goal
        "description": description,  # A short description of the goal
        "target_date": target_date,  # The date by which the goal should be achieved
        "current_savings": 0  # Initialize current savings towards the goal to 0
    }
    # Add the goal dictionary to the goals list
    goals.append(goal)
    # Print a message confirming the goal was set
    print(f"Goal Set: {description} - Save {amount} by {target_date}")

def add_savings_to_goal(goal_description, amount):
    '''This function adds savings towards a specific financial goal.'''
    # Loop through each goal in the goals list
    for goal in goals:
        # Check if the goal's description matches the one provided by the user
        if goal['description'] == goal_description:
            # Add the provided amount to the goal's current savings
            goal['current_savings'] += amount
            # Print a message confirming the savings were added
            print(f"Added {amount} to {goal_description}. Current savings: {goal['current_savings']}")

def monthly_expense_report(month, year):
    '''This function generates a report of expenses for a specific month and year.'''
    total_expense = 0  # Initialize total expense to 0
    # Loop through each transaction in the transactions list
    for transaction in transactions:
        # Convert the transaction's date from a string to a datetime object
        transaction_date = datetime.strptime(transaction['date'], "%Y-%m-%d")
        # Check if the transaction is an expense and if it occurred in the specified month and year
        if transaction['type'] == "expense" and transaction_date.month == month and transaction_date.year == year:
            # Add the transaction's amount to the total expense
            total_expense += transaction['amount']
            # Print the details of the expense
            print(f"Expense: {transaction['amount']} on {transaction['date']} - {transaction['description']}")
    # Print the total expenses for the specified month and year
    print(f"Total Expense for {month}/{year}: {total_expense}")

def visualize_income_vs_expense():
    '''This function visualizes income vs. expense over time using a line graph.'''
    # Extract dates and amounts from the transactions list
    dates = [datetime.strptime(t['date'], "%Y-%m-%d") for t in transactions]
    amounts = [t['amount'] if t['type'] == "income" else -t['amount'] for t in transactions]
    
    # Set up the plot
    plt.figure(figsize=(10, 5))
    # Plot the data: dates on the x-axis, amounts on the y-axis
    plt.plot(dates, amounts, label="Net Change", color='blue', marker='o')
    # Label the x-axis as "Date"
    plt.xlabel("Date")
    # Label the y-axis as "Amount"
    plt.ylabel("Amount")
    # Set the title of the graph
    plt.title("Income vs Expense Over Time")
    # Add a legend to the graph
    plt.legend()
    # Add a grid to the graph for better readability
    plt.grid(True)
    # Display the graph
    plt.show()

def save_data_to_file():
    '''This function saves the transactions and goals to a text file.'''
    # Combine the transactions and goals lists into a single dictionary
    data = {
        'transactions': transactions,
        'goals': goals
    }
    # Open a text file in write mode
    with open("finance_data.txt", "w") as file:
        # Convert the dictionary to a JSON string and write it to the file
        json.dump(data, file)
    # Print a message confirming the data was saved
    print("Data saved to finance_data.txt")

def load_data_from_file():
    '''This function loads the transactions and goals from a text file.'''
    try:
        # Open the text file in read mode
        with open("finance_data.txt", "r") as file:
            # Load the JSON string from the file and convert it back to a dictionary
            data = json.load(file)
            # Update the global transactions and goals lists with the loaded data
            global transactions, goals
            transactions = data['transactions']
            goals = data['goals']
        # Print a message confirming the data was loaded
        print("Data loaded from finance_data.txt")
    except FileNotFoundError:
        # If the file is not found, print an error message
        print("No saved data found.")

def main_menu():
    '''This function displays the main menu and handles user input.'''
    while True:
        # Print the menu options
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Calculate Balance")
        print("4. Set Financial Goal")
        print("5. Monthly Expense Report")
        print("6. Visualize Income vs Expense")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("9. Exit")
        # Prompt the user to choose an option
        choice = input("Choose an option: ")

        if choice == "1":
            # Option to add a transaction
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            type = input("Enter type (income/expense): ")
            add_transaction(amount, date, description, type)
        elif choice == "2":
            # Option to view all transactions
            view_transactions()
        elif choice == "3":
            # Option to calculate and display the balance
            calculate_balance()
        elif choice == "4":
            # Option to set a financial goal
            amount = float(input("Enter goal amount: "))
            description = input("Enter goal description: ")
            target_date = input("Enter target date (YYYY-MM-DD): ")
            set_goal(amount, description, target_date)
        elif choice == "5":
            # Option to generate a monthly expense report
            month = int(input("Enter month (MM): "))
            year = int(input("Enter year (YYYY): "))
            monthly_expense_report(month, year)
        elif choice == "6":
            # Option to visualize income vs. expense
            visualize_income_vs_expense()
        elif choice == "7":
            # Option to save data to a text file
            save_data_to_file()
        elif choice == "8":
            # Option to load data from a text file
            load_data_from_file()
        elif choice == "9":
            # Option to exit the program
            break
        else:
            # If the user enters an invalid option, print an error message
            print("Invalid choice. Please try again.")

# Start the program by displaying the main menu
main_menu()

