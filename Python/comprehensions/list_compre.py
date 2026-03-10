menu=[
  "masala chai",
  "iced lemon tea",
  "ginger tea",
  "lemon tea", 
  "iced peach tea"
]

iced_tea=[tea for tea in menu if "iced" in tea]
print(iced_tea)
iced_tea=[tea for tea in menu if len(tea)<16]
print(iced_tea)