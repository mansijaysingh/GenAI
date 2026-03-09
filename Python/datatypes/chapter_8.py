#List
ingredients=["water","milk","tea"]
ingredients.append("sugar")
print(f"Ingredients for chai:{ingredients}")
ingredients.remove("water")
print(f"Updated ingredients for chai:{ingredients}")

spice_option=["ginger","cardamom"]
chai_ingredients=["water","milk","tea"]
chai_ingredients.extend(spice_option)

print(f"Chai ingredients:{chai_ingredients}")
chai_ingredients.insert(2,"black tea")
print(f"Updated chai ingredients:{chai_ingredients}")

last_added=chai_ingredients.pop()
print(last_added)
print(chai_ingredients)

chai_ingredients.reverse()
print(f"Reversed chai ingredients:{chai_ingredients}")
chai_ingredients.sort()
print(f"sorted:{chai_ingredients}")

sugar_levels=[1,2,3,4,5,6]
print(f"maximum sugar level:{max(sugar_levels)}")
print(f"maximum sugar level:{min(sugar_levels)}")

  