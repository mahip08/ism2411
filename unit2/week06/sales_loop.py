sales = [120, 80, 250, 175, 90, 410, 60, 215]

for sale in sales:
    if sale >= 200:
        discount = 0.10
        discount_percent = 10
    elif sale >= 100:
        discount = 0.05
        discount_percent = 5
    else:
        discount = 0
        discount_percent = 0

    discounted_price = sale * (1 - discount)

    print(f"${sale} → {discount_percent}% discount → ${discounted_price:.2f}")