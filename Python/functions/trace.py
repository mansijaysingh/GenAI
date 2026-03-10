def add_vat(price, vat_rate):
  return price *(100+vat_rate)/100


orders=[100,150,200]

for order in orders:
  final_amount=add_vat(order,10)
  print(f"Final amount for order {order} is {final_amount}")