# interest_calculation.py

investment = int(input("Enter a investment amount (greater than 0 and less than 50000): "))
while investment <= 0 or investment >= 50000:
      print("Invalid amount. Please enter a value greater than 0 and less than 50000.")
      investment = int(input("Enter your investment amount:"))

rate = int(input("Enter the yearly interest rate (greater than 0 and less than 15): "))
while rate <= 0 or rate >= 15:
      print("Invalid rate. Please enter a value greater than 0 and less than 15.")
      rate = int(input("Enter the yearly interest rate:"))

years = int(input("Enter the duration of the investment in years (must be greater than 0): "))
while years <= 0:
      print("Invalid duration. Please enter a value greater than 0.")
      years = int(input("Enter the duration of the investment in years: "))

months = years * 12
monthly_rate = rate/12/100
total = 0

for month in range(1, months +1):
      total += investment
      interest = total * monthly_rate
      total += interest
      if month % 12 == 0:
            current_year = month // 12
            print(f"Year {current_year}: Investment value is ${total}")

print("\nFinal Summary:")
print(f"Total years: {years}")
print(f"Yearly interest rate: {rate}%")
print(f"Monthly investment amount: ${investment}")
print(f"Total amount after compounding: ${total}")

print("\nCompleted by, Jennifer Mendoza Trejo")
