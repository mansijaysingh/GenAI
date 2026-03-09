flavours=["Ginger","out of stock", "Lemon","Discontinued","Tulsi"]

for fla in flavours:
  if fla=="out of stock":
   continue
  if fla=="Discontinued":
    break
  print(f"{fla} item found")

print("End of the loop")
