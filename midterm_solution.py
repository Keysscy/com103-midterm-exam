
# Expense Tracker Program

# Step 1: Ask for name and budget
name = input("Student name: ")
budget = float(input("Weekly budget: "))

# Categories
categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

examples = [
    "Lunch, snacks, coffee",
    "Bus, jeepney, ride-share",
    "Load, data plan, WiFi top-up",
    "Notebook, pen, bond paper",
    "Games, movies, hangout"
]

print("\n==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")

# Step 2: Display categories using loop
i = 0
while i < len(categories):
    print(" " + str(i+1) + ". " + categories[i] + "       [e.g. " + examples[i] + "]")
    i = i + 1

print("==========================================")

# Storage
expense_list = []
total_spent = 0

# Step 3: Accept 4 expense entries
count = 1
while count <= 4:
    print("\n--- EXPENSE " + str(count) + " ---")
    cat = int(input("Category (0 to skip): "))

    if cat == 0:
        count = count + 1
        continue

    if cat >= 1 and cat <= 5:
        desc = input("Description: ")
        amount = float(input("Amount: "))

        # Step 5: Check 25% rule
        threshold = budget * 0.25
        alert = ""

        if amount > threshold:
            alert = "! High Expense Alert!"

        # Save expense
        expense_list.append([cat, desc, amount, alert])

        total_spent = total_spent + amount

    count = count + 1

# Step 6: Compute totals
remaining = budget - total_spent

if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

# Step 7: Print report
print("\n======================================================")
print("     " + name.upper() + " -- WEEKLY EXPENSE LOG")
print("======================================================")

print("  Weekly Budget  : P" + format(budget, ".2f"))

i = 0
entry_num = 1
while i < len(expense_list):
    cat = expense_list[i][0]
    desc = expense_list[i][1]
    amount = expense_list[i][2]
    alert = expense_list[i][3]

    print("  [" + str(entry_num) + "] " + categories[cat-1])
    print("      " + desc + "              P" + format(amount, ".2f") + "  " + alert)

    entry_num = entry_num + 1
    i = i + 1

print("------------------------------------------------------")
print("  Total Spent    : P" + format(total_spent, ".2f"))
print("  Remaining      : P" + format(remaining, ".2f"))
print("  Status         : " + status)
print("======================================================")