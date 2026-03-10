def make_chai():
  return "Here is your masala chai"

return_value=make_chai()

print(return_value)


def idle_chaiwala():
  pass

print(idle_chaiwala())


def sold_cup():
  return 120

total=sold_cup()
print("Total:",total)


def chai_status(cups_left):
  if cups_left==0:
    return "Sorry, we are out of chai"
  return "chai is ready"
  print("chai")# the code after return will not be executed

print(chai_status(0))
print(chai_status(6))


def chai_report():
  return 100,20,30

sold, remaining, not_paid=chai_report()
print("sold:",sold)
print("remaining:",remaining)
print("not paid:",not_paid)