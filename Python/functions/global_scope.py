chai_type="Plain" #global scope

def front_desk():
  def kitchen():
    global chai_type
    chai_type="Irani"
  kitchen()

front_desk()
print("final:",chai_type)