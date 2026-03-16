import threading
import time


def boil_milk():
  print("Boiling milk...")
  time.sleep(2)
  print("milk boiled...")

def toast_bun():
  print("toasting bun...")
  time.sleep(3)
  print("done with bun toasting...")

start=time.time()

t1=threading.Thread(target=boil_milk)
t2=threading.Thread(target=toast_bun)

t1.start()
t2.start()
t1.join()
t2.join()

end=time.time()

print(f"Breakfast is ready in {end-start:.2f} seconds")