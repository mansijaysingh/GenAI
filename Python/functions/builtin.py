def chai_flavor(flavor="Ginger"):
  """return the flavor of chai"""
  return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)

def generate_bill(chai=0, samosa=0):
  """generate bill for chai and samosa
  :param chai: number of cups of chai
  :param samosa: number of samosas
  :return: total bill"""
  total=chai*10 +samosa*20
  return total, "Thakyou for visiting "

print(generate_bill.__doc__)
print(generate_bill.__name__)