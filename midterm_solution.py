name = input("Student name: ")
budget = float(input("Weekly budget: "))

categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

print("\n==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")

for i in range(len(categories)):
    print(" " + str(i+1) + ". " + categories[i])

print("==========================================\n")

expenses = []
total_spent = 0

for i in range(1, 5):
    print("--- EXPENSE " + str(i) + " ---")
    cat_num = int(input("Category (0 to skip): "))

    if cat_num == 0:
        continue

    
    if cat_num >= 1 and cat_num <= 5:
        desc = input("Description: ")
        amount = float(input("Amount: "))

        if amount > 0.25 * budget:
            flag = "! High Expense Alert!"
        else:
            flag = ""

        expenses.append([cat_num, desc, amount, flag])
        total_spent = total_spent + amount

    print()

remaining = budget - total_spent

if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

print("\n======================================================")
print("     " + name.upper() + " -- WEEKLY EXPENSE LOG")
print("======================================================")

print("  Weekly Budget  : P" + format(budget, ".2f"))

count = 1
for exp in expenses:
    cat = categories[exp[0] - 1]
    desc = exp[1]
    amt = exp[2]
    flag = exp[3]

    print("  [" + str(count) + "] " + cat)
    print("      " + desc.ljust(30) + " P" + format(amt, ".2f") + " " + flag)
    count = count + 1

print("------------------------------------------------------")
print("  Total Spent    : P" + format(total_spent, ".2f"))
print("  Remaining      : P" + format(remaining, ".2f"))
print("  Status         : " + status)
print("======================================================")