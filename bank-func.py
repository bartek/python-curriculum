# Make a bank.
"""
Banks will have three functions. Let's start the kids off and then they will be
c hallenged to complete the other functions.
"""

print("Welcome to Space Bank! For all your inter-galactic needs!")

total_cash = 0

def deposit(current_cash, amount):
  return current_cash + amount

while True:
  print("1 - Deposit")
  print("2 - Withdrawal")
  print("3 - Space Cash Balance")

  command = str(input("What would you like to do? "))
  if command == "1":
    amount = int(input("How much space bucks would you like to deposit? "))
    total_cash = deposit(total_cash, amount)
    print("Thank you! You now have %s " % total_cash)
  else:
    break
