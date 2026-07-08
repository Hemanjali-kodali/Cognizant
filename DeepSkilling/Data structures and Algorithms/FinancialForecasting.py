def forecast(amount, rate, years):
    if years == 0:        
        return amount
    return forecast(amount * (1 + rate / 100), rate, years - 1)

current_amount = float(input("Enter current amount: "))
growth_rate = float(input("Enter annual growth rate (%): "))
years = int(input("Enter number of years: "))

future_value = forecast(current_amount, growth_rate, years)

print("Future Value =", round(future_value, 2))