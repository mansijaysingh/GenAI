def brew_chai(fla):
 if fla not in ["masala","ginger","lemon"]:
  raise ValueError("Unsupported chai flavor....")
 
 print(f"brewing {fla} chai....")


brew_chai("mint")
