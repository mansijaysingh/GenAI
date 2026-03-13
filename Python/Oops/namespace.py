class Chai:
  origin="India"

print(Chai.origin)

Chai.is_hot=True

print(Chai.is_hot)

#Creating objects from class chai

Masala=Chai()
print(f"Masala:{Masala.origin}")
print(f"Masala is hot:{Masala.is_hot}")
Masala.flavor="masala"
print(f"flavor of masala tea:{Masala.flavor}")

