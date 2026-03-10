# chai="Ginger chai"

# def prep_chai(order):
#   print("preparing:",order)

# prep_chai(chai)
# print(chai)


chai=[1,2,3]
def edit_chai(cups):
  cups[1]=42
edit_chai(chai)
print(chai)


def make_chai(tea,milk,sugar):
  print(tea,milk,sugar)

make_chai("Darjeeling","yes","Low")
#positional arguments
make_chai(tea="green",milk="no",sugar="no")

def specail_chai(*ingredients,**extras):
  print("ingredients:",ingredients)
  print("extras:",extras)

specail_chai("cinnamon","cardamom",sweetener="honey",milk="yes")


# def chai_order(order=[]):
#   order.append("Masala Chai")
#   print(order)
# chai_order()
# chai_order()


def chai_order(order=None):
  if order is None:
    order=[]
    order.append("ginger chai")
    print(order)

chai_order()
chai_order()