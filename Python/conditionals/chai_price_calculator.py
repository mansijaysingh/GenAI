user=input("Enter Your cup size(small/medium/large):").lower()

if user=="small":
  print(f"Price is 10 rupees.")
elif user=="medium":
  print("Price is 20 rupees.")
elif user=="large":
  print("Price is 30 rupees.")
else:
  print("Invalid size. Please choose small, medium, or large.")