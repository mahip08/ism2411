# Exercise 5: Anomaly flagging

amount = float(input("Enter transaction amount: $"))

if amount <= 0:
    print("SUSPICIOUS")
elif amount >= 10000:
    print("LARGE — REVIEW REQUIRED")
else:
    print("NORMAL")