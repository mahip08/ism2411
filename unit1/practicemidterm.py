miles=240

if miles <50:
    rate=0
elif miles<200:
    rate=0.40
elif miles <500:
    rate=0.50
else:
    rate=0.60

reimbursement=miles*rate
if reimbursement>=100:
    meal=30
else:
    meal=0

total=reimbursement+meal

print("Reimbursement:",reimbursement)
print("Meal allowance:", meal)
print("Total Paid:", total)
