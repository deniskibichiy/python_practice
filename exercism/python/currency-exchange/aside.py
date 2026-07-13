def exchangeable_value(budget, exchange_rate, spread, denomination):
    amount_after_exchange = budget/exchange_rate
    print(amount_after_exchange)
    amount_after_deduction = amount_after_exchange * (100-spread)/100
    print(amount_after_deduction)
    return int((amount_after_deduction/ denomination) * denomination)
print(exchangeable_value(1500, 0.84, 25, 40))

#budget=1500, exchange_rate=0.84, spread=25, denomination=40, expected=1400)
