def serve_chai():
  chai_type="Masala"#local scope
  print(f"Inside function:{chai_type}")


chai_type="lemon"#global scope
print(f"Outside function:{chai_type}")
serve_chai()


def chai_counter():
  chai_order="lemon"
  
  def print_order():
    chai_order="ginger"
    print(f"inner:{chai_order}")
  
  print_order()
  print(f"outer:{chai_order}")

chai_order="Black"
print(f"Global:{chai_order}")
chai_counter()
