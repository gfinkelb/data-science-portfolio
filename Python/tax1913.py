
income = float(input("Enter your income: "))

if income <= 50000:
    tax = income * 0.01
elif income <= 75000:
    tax = 50000 * 0.01 + (income - 50000) * 0.02
elif income <= 100000:
    tax = 50000 * 0.01 + 25000 * 0.02 + (income - 75000) * 0.03
elif income <= 250000:
    tax = 50000 * 0.01 + 25000 * 0.02 + 25000 * 0.03 + (income - 100000) * 0.04
elif income <= 500000:
    tax = 50000 * 0.01 + 25000 * 0.02 + 25000 * 0.03 + 150000 * 0.04 + (income - 250000) * 0.05
elif income > 500000:
    tax = 50000 * 0.01 + 25000 * 0.02 + 25000 * 0.03 + 150000 * 0.04 + 250000 * 0.05 + (income - 500000) * 0.06
    
print(f"Your income tax is: ${tax}")

input("Press Enter to exit...")    