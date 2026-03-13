class Chai:
  temp="Hot"
  strength="Strong"

cutting=Chai()
print(cutting.temp)

cutting.temp="mild"
print(f"After chnaging",cutting.temp)
print(f"Direct look into the class",Chai.temp)

del cutting.temp
print(cutting.temp)