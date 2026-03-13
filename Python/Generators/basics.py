def serve_chai():
  yield "cup1: Masala chai"
  yield "cup2: Ginger chai"
  yield "cup3: Elaichi chai"


stall=serve_chai()
for cup in stall:
  print(cup)


def get_chai_list():
  return ["cup1", "cup2", "cup3"]

def get_chai_gen():
  yield "cup1"
  yield "cup2"
  yield "cup3"

chai=get_chai_gen()
print(next(chai))