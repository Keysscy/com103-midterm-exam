# EXPENSE TRACKER (BEGINNER VERSION)

print("==========================================")
print("       WEEKLY EXPENSE TRACKER")
print("==========================================")

# Ask for name
name = input("Enter your name: ")

# Budget input with validation (NUMBERS ONLY)
while True:
    budget_input = input("Enter your weekly budget (numbers only): ")

    if budget_input.isdigit():
        budget = int(budget_input)
        break
    else:
        print("Invalid input, please enter a proper number")

print(" ")

# Expense categories
print("==========================================")
print(" WEEKLY EXPENSE -- CATEGORIES ")
print("==========================================")

print("1. Food & Drinks [Lunch, snacks, coffee]")
print("2. Transportation [Bus, jeepney, ride-share]")
print("3. Mobile / Internet [Load, data, WiFi]")
print("4. School Supplies [Notebook, pen, paper]")
print("5. Entertainment [Games, movies, hangout]")

print("==========================================")

# Lists to store data
category_list = []
description_list = []
amount_list = []
alert_list = []

total_spent = 0

# 25% threshold
threshold = budget * 25 / 100

# Ask for 4 expenses
i = 1
while i <= 4:
    print(" ")
    print("--- EXPENSE", i, "---")

    # Category input
    while True:
        cat_input = input("Category (0 to skip): ")

        if cat_input.isdigit():
            category = int(cat_input)

            if category >= 0 and category <= 5:
                break
            else:
                print("Invalid category. Please enter 0 to 5 only.")
        else:
            print("Invalid input. Please enter a number.")

    # Skip option
    if category == 0:
        category_list.append("SKIPPED")
        description_list.append("SKIPPED")
        amount_list.append(0)
        alert_list.append("")
        i = i + 1
        continue

    # Description
    desc = input("Description: ")

    # Amount input validation
    while True:
        amt_input = input("Amount: ")

        if amt_input.isdigit():
            amount = int(amt_input)
            break
        else:
            print("Invalid input. Please enter a number.")

    # Check high expense
    alert = ""
    if amount > threshold:
        alert = "! High Expense Alert!"

    # Store data
    category_list.append(category)
    description_list.append(desc)
    amount_list.append(amount)
    alert_list.append(alert)

    total_spent = total_spent + amount

    i = i + 1


# Remaining balance
remaining = budget - total_spent

# Budget status
status = ""
if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

print(" ")
print("======================================================")
print(name, "-- WEEKLY EXPENSE LOG")
print("======================================================")

print("Weekly Budget : P", budget)
print(" ")

# Print expenses
j = 0
display_number = 1

while j < 4:

    if category_list[j] != "SKIPPED":

        print("[", display_number, "] Category:", category_list[j])
        print("    Description:", description_list[j])
        print("    Amount: P", amount_list[j])

        if alert_list[j] != "":
            print("    ", alert_list[j])

        display_number = display_number + 1

    j = j + 1

print("------------------------------------------------------")
print("Total Spent : P", total_spent)
print("Remaining   : P", remaining)
print("Status      : ", status)
print("======================================================")