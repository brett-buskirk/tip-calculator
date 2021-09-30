# Set static sales tax
tax = 0.10


def get_user_input(inst_type, msg):
  """Function to insure user input is in correct data type"""
  # Make sure user_input is not a number initially
  user_input = ""
  # Keep prompting user until correct value type is given
  while not isinstance(user_input, inst_type):
    try:
      # If input can be converted to expected type, continue
      user_input = inst_type(input(msg))
      # If input is equal to or less than 0, raise an exception
      if user_input <= 0:
        raise
    except:
      # If exception is raised, print message and reset user_input
      print('Please use a positive number only')
      user_input = ""
  # If all is well, return the user input
  return user_input


# Declare input variables by passing them through the function
bill = get_user_input(float, "How much is the bill? ")
people = get_user_input(int, "How many people are splitting the bill? ")
tip = get_user_input(float, "What percentage will you be tipping? ")

# Calculate the total sales tax
tax_amount = round(tax * bill, 2)

# Calculate the total tip amount
tip_amount = round((tip / 100) * bill, 2)

# Figure the total bill
total_bill = round(bill + tax_amount + tip_amount, 2)

# Calculate the total per person
total_each = round(total_bill / people, 2)

# Output the results in a formatted block
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
