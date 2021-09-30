# Set static sales tax
tax = 0.10

# Function to get user input in the correct data type
def get_user_input(inst_type, msg):
  user_input = ""
  while not isinstance(user_input, inst_type):
    try:
      user_input = inst_type(input(msg))
      if user_input <= 0: raise
    except:
      print('Please use a positive number only')
      user_input = ""
  return user_input

# Declare initial user input variables
bill = get_user_input(float, "How much is the bill? ")
people = get_user_input(int, "How many people are splitting the bill? ")
tip = get_user_input(float, "What percentage will you be tipping? ")

# Set tip as percentage
tip_percent = tip / 100

# Calculate the total sales tax
tax_amount = tax * bill

# Calculate the total tip amount
tip_amount = tip_percent * bill

total_bill = bill + tax_amount + tip_amount

# Calculate the total per person
total_each = total_bill / people
total_each = "{:.2f}".format(total_each)

# Output the results
print('\n==========================================')
print(f'\tBILL RESULTS ({people} people)')
print('==========================================')
print(f"Meal Cost: \t\t${bill}")
print(f"Sales Tax: \t\t${tax_amount}")
print(f"{tip}% Tip: \t\t${tip_amount}")
print("==========================================")
print(f"Total Bill: \t\t${total_bill}")
print("==========================================")
print(f"Cost per Person: \t${total_each}\n")