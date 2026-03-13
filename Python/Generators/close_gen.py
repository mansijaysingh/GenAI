def local_chai():
  yield "Masala chai"
  yield "Adrak chai"

def imported_chai():
  yield "matcha Tea"
  yield "Oolong Tea"


def full_menu():
  yield from local_chai()
  yield from imported_chai()

for chai in full_menu():
  print(chai)

def chai_stall():
 try:
   while True:
     order= yield "waiting for the order"
 except:
   print("stall is closed")

stall=chai_stall()
print(next(stall))
stall.close()
