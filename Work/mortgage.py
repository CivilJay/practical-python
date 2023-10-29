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
    principal = (principal * (1+rate/12)) - (payment)
    total_paid = total_paid + payment
    month = month + 1

    # Test for extra payment and applies the payment 
    if ExtraPayment > 0:
        while (month >= ExtraPaymentStartMonth and month <= ExtraPaymentEndMonth):
           # print ('zone', end='')  for debugging 
            principal = principal - ExtraPayment
            total_paid = total_paid + ExtraPayment
            break
        else:
            pass
   
   # code to correct for the over payment; the overpayment is negated
    if principal < 0:
        total_paid = total_paid + principal
        principal = principal - principal

    #print(month,total_paid, principal,)
    roundPrinc = round(principal,2)
    roundTotal = round(total_paid,2)
    sen = f'Month {month}, total paid is {roundTotal}, and loan amount is {roundPrinc}'
    print(sen)
''' bool ('false') Evaluates to  True becuase a string is present 

If the string were empty then converting it to a Bool as in:
bool('') would evaluate to False
'''
