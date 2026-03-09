staff=[("Amit", 16), ("Sara", 22), ("Mike", 18), ("Becky", 25)]
for name , age in staff:
  if age<=18:
    print(f"{name} is eligible to work at the tea stall.")
    break
else:
  print("No eligible staff found for the tea stall.")