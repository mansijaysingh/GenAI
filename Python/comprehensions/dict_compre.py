tea_prices_inr={
    'green': 100,
    'black': 150,
    'oolong': 200
}

# Convert the prices to USD 
tea_price_usd={tea:price/80 for tea,price in tea_prices_inr.items()}
print(tea_price_usd)