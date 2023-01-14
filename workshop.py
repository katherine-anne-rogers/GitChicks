numCategories = input(f'How many categories would you like to budget for?\n')
if not numCategories.isnumeric():
    numCategories = input(
        "Invalid response - Please enter an integer.\nHow many categories would you like to budget for?\n")

print('\n')

listOfCatergories = []
listNames = []

for x in range(int(numCategories)):
    nameOfCategory = input("What would you like to name your category?\n")
    listOfCatergories.append([nameOfCategory])
    listNames.append(nameOfCategory)

print('\n')

print(f'Your categories are:')
for item in listOfCatergories:
    print(f'- {item[0]}')

print('\n')

for item in listOfCatergories:
    budget = input(("What is your budget for {}?\n".format(item[0])))
    if budget.isnumeric():
        item.append(int(budget))
        categorySpent = 0
        item.append(categorySpent)
    else:
        budget = input("Invalid response - Please enter an integer.\nWhat is your budget for {}?\n".format(item[0]))
print('\n')

purchaseCategory = input("Which category was your purchase in? (Or press enter to finish adding purchases.)\n")

while purchaseCategory != "":
    if purchaseCategory in listNames:
        for item in listOfCatergories:
            if purchaseCategory == item[0]:
                purchaseAmount = input("How much did you spend?\n")
                purchaseAmount = int(purchaseAmount)
                item[2] += purchaseAmount
    else:
        print("That is not a category! Please select from the following:")
        for item in listNames:
            print(f'- {item[0]}')
    purchaseCategory = input("Which category was your purchase in? (Or press enter to finish adding purchases.)\n")
print('\n')

for item in listOfCatergories:
    budgetLeft = item[1] - item[2]
    item.append(budgetLeft)

totalSpent = 0
for item in listOfCatergories:
    totalSpent += item[2]

print(f'Your total spending was ${totalSpent}.')
for item in listOfCatergories:
    print(f'Your total spending for {item[0]} was ${item[2]}.')
    if item[3] > 0:
        print(f'You underspent your {item[0]} bugdet by ${item[3]}.')
    elif item[3] == 0:
        print(f'Your spent your {item[0]} budget perfectly!')
    elif item[3] < 0:
        print(f'You overspent your {item[0]} budget by ${item[3]}.')
