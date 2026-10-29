weekly_pay = float(input("Enter the week's take-home pay: "))

print(f"Weekly Pay: ${weekly_pay}")

weekly_bills = {"groceries":265, "truck food":60, "snowball":100, "moving":50}

total_committed = sum(weekly_bills.values())

print(f"Total Committed: ${total_committed}")

for item, cost in weekly_bills.items():
    print(f"{item}: ${cost}")

cushion = round(weekly_pay - total_committed, 2)

print(f"Cushion: ${cushion}")

if cushion < 0:
    print(f"Short by ${abs(cushion)}")