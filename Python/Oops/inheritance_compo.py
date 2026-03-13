class Basechai:
  def __init__(self,type_):
    self.type=type_

  def prepare(self):
    print(f"preparing{self.type} chai....")

class MasalaChai(Basechai):
  def add_spices(self):
    print("adding cardamom, ginger,cloves.")

class Chaishop:
  chai_cls=Basechai
  def __init__(self):
    self.chai=self.chai_cls("Regular")

  def serve(self):
    print(f"serving {self.chai.type} chai in the shop")
    self.chai.prepare()

class FancyChaiShop(Chaishop):
  chai_cls=MasalaChai

shop=Chaishop()
fancy=FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()