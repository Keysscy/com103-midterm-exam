# Expense Tracker - Beginner Version

print("WELCOME TO EXPENSE TRACKER")
print("----------------------------")

# Get student name
name = input("Enter your name: ")

# Get valid budget (must be numeric)
while True:
    budget_input = input("Enter your weekly budget: ")
    try:
        budget = float(budget_input)
        break
    except:
        print("Invalid input, please enter a proper number.")

# Expense categories
categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

print("")
print("==========================================")
print("WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")

i = 0
while i < 5:
    print(i + 1, ".", categories[i])
    i = i + 1

print("==========================================")
print("")

# storage for expenses
exp_category = []
exp_description = []
exp_amount = []
exp_flag = []

total_spent = 0

count = 1

# loop for 4 expenses
while count <= 4:
    print("--- EXPENSE", count, "---")

    cat_input = input("Category (0 to skip): ")

    try:
        cat = int(cat_input)
    except:
        print("Invalid category input, skipped.")
        cat = 0

    if cat == 0:
        print("")
        count = count + 1
        continue

    if cat < 1 or cat > 5:
        print("Invalid category number, skipped.")
        print("")
        count = count + 1
        continue

    desc = input("Description: ")
    amt_input = input("Amount: ")

    try:
        amt = float(amt_input)
    except:
        print("Invalid amount, skipped.")
        print("")
        count = count + 1
        continue

    exp_category.append(cat)
    exp_description.append(desc)
    exp_amount.append(amt)

    limit = budget * 0.25

    if amt > limit:
        exp_flag.append("! High Expense Alert!")
    else:
        exp_flag.append("")

    total_spent = total_spent + amt

    print("")
    count = count + 1

# remaining balance
remaining = budget - total_spent

# status
if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

# OUTPUT REPORT
print("")
print("======================================================")
print(name, "-- WEEKLY EXPENSE LOG")
print("======================================================")

print("Weekly Budget : P", budget)

i = 0
while i < 4:
    if i < len(exp_category):
        print("[", i + 1, "] ", categories[exp_category[i] - 1], sep="")
        print("     ", exp_description[i])
        print("     P", exp_amount[i])

        if exp_flag[i] != "":
            print("     ", exp_flag[i])

    i = i + 1

print("------------------------------------------------------")
print("Total Spent : P", total_spent)
print("Remaining   : P", remaining)
print("Status      : ", status)
print("======================================================")