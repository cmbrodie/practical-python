# mortgage.py
#
# Exercise 1.7

principal = 500_000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 5
extra_payment_end_month = 9
extra_payment = 1000
while principal > 0:
    extra = payment + extra_payment
    if principal < payment:
        payment = principal * (1 + rate / 12)
    elif extra_payment_start_month <= month < extra_payment_end_month:
        payment = extra
    else:
        payment = 2684.11
    principal = principal * (1 + rate / 12) - payment
    total_paid += payment
    month += 1
    print(
        f"month: {month}, total_paid: ${total_paid:0.2f}, principal: ${principal:0.2f}"
    )

print(f"Total paid: {total_paid:.2f}")
