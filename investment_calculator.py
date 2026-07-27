money = float(input("Investment amount: "))
growth = float(input("Expected growth %: "))

profit = money * growth / 100

total = money + profit

print("Profit:", profit)
print("Total:", total)
