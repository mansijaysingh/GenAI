user=input("Enter your preferrence for seat(sleeper/Ac/general/luxury):").lower()

match user:
  case "sleeper":
    print("You have selected Sleeper class. No AC, beds available!")
  case "ac":
    print("You have selected AC class. Air conditioned, comfy ride!")
  case "general":
    print("You have selected General class. Cheapest option, no reservation!")
  case "luxury":
    print("You have selected Luxury class. Premium seats with meals!")
  case _:
    print("Invalid seat preference. Please choose from sleeper, AC, general, or luxury.")