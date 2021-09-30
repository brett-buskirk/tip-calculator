# Set static sales tax
tax = 0.10

# Declare initial user input variables
bill = ""
people = ""
tip = ""

# Grab and format user input for bill, looping until correct type is given
while not isinstance(bill, float):
  try:
    bill = float(input("How much is the bill? "))
    if bill <= 0: raise
  except:
    print('Please use a positive number only')
    bill = ""

# Grab and format user input for people, looping until correct type is given
while not isinstance(people, int):
  try:
    people = int(input("How many people are splitting the bill? "))
    if people <= 0: raise
  except:
    print('Please use a positive integer only')
    people = ""

# Grab and format user input for tip, looping until correct type is given
while not isinstance(tip, float):
  try:
    tip = float(input("What percent will you be tipping? "))
    if tip <= 0: raise
  except:
    print('Please use a positive integer only')
    tip = ""

# Set tip as percentage
tip_percent = tip / 100

# Calculate the total sales tax
tax_amount = tax * bill

# Calculate the total tip amount
tip_amount = tip_percent * bill

total_bill = bill + tax_amount + tip_amount

# Calculate the total per person
total_each = total_bill / people

# Output the results
print('\n=======================================')
print('\t\t\t BILL RESULTS')
print('=======================================')
print(f"Meal Cost: \t\t${bill}")
print(f"Sales Tax: \t\t${tax_amount}")
print(f"{tip}% Tip: \t\t${tip_amount}")
print("=======================================")
print(f"Total Bill: \t\t${total_bill}")
print("=======================================")
print(f"Cost per Person: \t${total_each}")