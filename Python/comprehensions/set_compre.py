favourite_chais=[
  "Masala Chai",
  "Ginger Chai",
  "Cardamom Chai",
  "Masala Chai",
  "Ginger Chai",
  "Cardamom Chai"
]

unique_chai={ chai for chai in favourite_chais }
print(unique_chai)

recipes={
  "masala chai": ["water", "milk", "tea leaves", "spices"],
  "ginger chai": ["water", "milk", "tea leaves", "ginger"],
  "cardamom chai": ["water", "milk", "tea leaves", "cardamom"]
}

unique_spices={ ing for spice in recipes.values() for ing in spice}
print(unique_spices)