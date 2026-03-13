def chai_customer():
  print("welcome! what would you like to have?")
  order=yield
  while True:
   print(f"preparing {order} for you")
   order=yield

stall=chai_customer()
next(stall)
stall.send("pizza and cold drinks")