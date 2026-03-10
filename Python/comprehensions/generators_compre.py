daily_sales=[5,10,15,20,9,8,4,7,3,2,1]

total_cups=sum(sale for sale in daily_sales if sale>5)
print(total_cups)