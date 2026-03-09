value=13

if remainder:=value%5:
  print(f"Not divisible, remainder is {remainder}")


availble_sizes=["Small","Medium","Large"].lower()
if (requested_size:=input("Enter your cup size:"))in availble_sizes:
  print(f"{requested_size} size is available.")
else: 
  print(f"Sorry, {requested_size} size is not available. Please choose from {availble_sizes}.") 
