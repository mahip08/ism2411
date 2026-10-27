#Exercise 1: 
price =50
quantity = 12
revenue= price * quantity

print(f"Revenue: ${revenue:,.2f}")






# Excercise 2:

cost = 32
price = 50
margin = (price - cost) / price
print(f"Margin: {margin: .1%}")


# Exercise 3: Boolean Logic
# Product A wins if margin_a > margin_b
# Product A margin 60%, Product B margin (80-60)/80 = 25%
# Product A
price_a = 50
cost_a = 12
margin_a = price_a - cost_a

# Product B
price_b = 50
cost_b = 32
margin_b = price_b - cost_b

# Compare margins
product_a_wins = margin_a > margin_b

# Print results
print("Product A margin:", margin_a)
print("Product B margin:", margin_b)
print("Is Product A's margin higher?", product_a_wins)



# Exercise 4: Logic Combo

is_premium = price > 100 and margin > 0.3
print(f"Is Premium: {is_premium}")

price = 150
margin = .2

#Exercise 5: Division + Mod

print(17/3)
print(17//3)
print(17%3)

# Exercise 7

BOX_SIZE = 24
items_ordered = int(input("Number of items ordered: "))
full_boxes = items_ordered // BOX_SIZE
loose_items = items_ordered % BOX_SIZE
exact_fit = loose_items == 0
print(f"Full bxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")


# Exercise 6

def calc_discount(price, rate):
    return price * (1-rate)

print(calc_discount(100, int(8/100)))

discounted_pct = 20
discounted_rev = revenue * (1 - discounted_pct / 100)

print(discounted_rev)

# inputs name, retail_price, cost, quantity_sold, discount_pct

product = input("Enter the product name: ")
retail_price = float(input("Enter the retail price: "))
quantity_sold = int(input("Enter the quantity sold "))
discount_pct = int(input("Enter the discount percentage: "))
cost = float(input("Enter the cost: "))

revenue = retail_price * quantity_sold
discounted_revenue = revenue * (1-discounted_pct / 100)
gross_margin = (retail_price - cost) / retail_price
net_profit = discounted_revenue - (cost *quantity_sold)

print(f"Product: {product}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Discounted Revenue: ${discounted_revenue:,.2f}")
print(f"Gross Margin: {gross_margin: .1%}")
print(f"Net Profit: ${net_profit:,.2f}")
