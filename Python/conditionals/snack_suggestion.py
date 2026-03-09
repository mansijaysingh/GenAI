snack=input("Enter your preferred snack:").lower()

print(f"user said:{snack}")

if snack=="cookies" or snack=="samosa":
  print(f"Great choice! We'll prepare {snack} for you.")
else:
  print(f"Sorry, we don't have {snack}. Please choose either cookies or samosa.")