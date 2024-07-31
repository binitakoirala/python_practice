#
# Write a function calculate_monthly_payment(principal, rate, years) that calculates and returns the monthly payment for a loan given the principal amount, interest rate, and loan duration in years.
def calculate_monthly_payment(principal, rate, years):
    """
    Calculate the monthly payment for a loan.

    Args:
        principal (float): The principal amount of the loan.
        rate (float): The interest rate of the loan (in decimal form, e.g. 5% = 0.05).
        years (int): The duration of the loan in years.

    Returns:
        float: The monthly payment amount.
    """
    monthly_rate = rate / 12
    loan_term = years * 12
    
    pay = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** (-loan_term)) # ** represents power.
    return round(pay, 2)

monthly_payment = calculate_monthly_payment(20000, 5, 5)
print(f"The monthly payment is: £{monthly_payment}")
