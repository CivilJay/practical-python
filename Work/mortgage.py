# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
ExtraPaymentStartMonth = 61
ExtraPaymentEndMonth = 108
ExtraPayment = 1000

month = 0
while principal > 0:
    if ExtraPayment > 0:
        if (month >= ExtraPaymentStartMonth & month <= ExtraPaymentEndMonth):
            principal = principal * (1+rate/12) - (payment+ExtraPayment)
            total_paid = total_paid + payment
            month = month + 1
            print(month,total_paid)
        else: 
            pass
    principal = principal * (1+rate/12) - (payment)
    total_paid = total_paid + payment
    month = month + 1
    print(month,total_paid)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month = month + 1
print('Total paid', total_paid,'in', month,'months')