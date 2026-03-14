def ServeChai(fla):
  try:
    print(f"preparing {fla} chai....")
    if fla=="unknown":
      raise ValueError("we dont know that flavor")
  except ValueError as e:
    print("Error",e)
  else:
    print(f"{fla}chai is serve")
  finally:
    print("next customer please")


ServeChai("masala")
ServeChai("unknown")
  
