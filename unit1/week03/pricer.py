product = "laptop"
unit_price = 499.99
quantity = 3
unit_cost = 329
in_stock = True
print(type(product))
print(type(unit_price))
print(type(quantity))
print(type(in_stock))
print(f"{quantity} units of {product} at {unit_price} each = ${unit_price*quantity:.2f}")
product = input("Enter product: ")
unit_price = float(input("Enter price: "))
quantity = int(input("Enter quantity "))
print(f"{quantity} units of {product} at ${unit_price} each = ${unit_price * quantity:.2f}")

revenue = unit_price * quantity
margin = (unit_price - unit_cost) / unit_price * 100
print(f"Product: {product}")
print(f"Price: ${unit_price:.2f}")
print(f"Qty: {quantity}")
print(f"Revenue: ${revenue:.2f}")
print(f"Margin: {margin:.1f}%")
