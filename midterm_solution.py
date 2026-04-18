
categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

print("==========================================")
print("WELCOME TO WEEKLY EXPENSE TRACKER")
print("==========================================")


name = input("Enter your name: ")


while True:
    budget_input = input("Enter your weekly budget: ")

    valid = True

    if budget_input == "":
        valid = False
    else:
        for ch in budget_input:
            if ch < "0" or ch > "9":
                valid = False

    if valid == True:
        budget = int(budget_input)
        break
    else:
        print("Invalid input, please enter a proper number")


print("")
print("==========================================")
print("EXPENSE CATEGORIES")
print("==========================================")

for i in range(5):
    print(str(i + 1) + ". " + categories[i])

print("==========================================")


expenses = []
expense_count = 0


threshold = budget * 25 / 100


for i in range(4):

    print("")
    print("--- EXPENSE " + str(i + 1) + " ---")

    category_input = input("Category (0 to skip): ")

    valid_cat = True

    if category_input == "":
        valid_cat = False
    else:
        for ch in category_input:
            if ch < "0" or ch > "9":
                valid_cat = False

    if valid_cat == True:
        category = int(category_input)
    else:
        category = -1

    if category == 0:
        print("Skipped expense slot")
    else:
        if category >= 1 and category <= 5:

            description = input("Description: ")

            while True:
                amount_input = input("Amount: ")

                valid_amount = True

                if amount_input == "":
                    valid_amount = False
                else:
                    for ch in amount_input:
                        if ch < "0" or ch > "9":
                            valid_amount = False

                if valid_amount == True:
                    amount = int(amount_input)
                    break
                else:
                    print("Invalid input, please enter a proper number")

            flag = ""

            if amount > threshold:
                flag = "! High Expense Alert!"

            expense = [category, description, amount, flag]
            expenses.append(expense)

            expense_count = expense_count + 1

        else:
            print("Invalid category, skipped")


print("")
print("======================================================")
print(name.upper() + " -- WEEKLY EXPENSE LOG")
print("======================================================")

print("Weekly Budget : P" + str(budget))

total = 0
count = 0

for item in expenses:
    count = count + 1

    cat_num = item[0]
    desc = item[1]
    amt = item[2]
    tag = item[3]

    print("")
    print("[" + str(count) + "] " + categories[cat_num - 1])
    print(desc)
    print("P" + str(amt))

    if tag != "":
        print(tag)

    total = total + amt

remaining = budget - total

print("")
print("------------------------------------------------------")
print("Total Spent : P" + str(total))
print("Remaining : P" + str(remaining))

if remaining >= 0:
    print("Status : Budget OK! Keep it up.")
else:
    print("Status : Overspent! Reduce spending.")

print("======================================================")