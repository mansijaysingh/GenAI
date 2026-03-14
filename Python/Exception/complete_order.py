class InvalidChaiError(Exception):pass


def bill(fla,cups):
  menu={"masala":20, "ginger":40}
  try:
    if fla not in menu:
      raise InvalidChaiError("That chai is not available")
    if not isinstance(cups,int):
      raise TypeError("Numbers of cups must be an integer")
    total=menu[fla]*cups
    print(f"Your bill for {cups} cups of {fla} chai: rupees {total}")

  except Exception as e:
    print("Error:",e)
  finally:
    print("Thankyou for visiting our cafe")

bill("lemon",4)
bill("masala","two")
bill("ginger",2)

