chai_menu={"masala":30,"ginger":40}
try:

 chai_menu["Lemon"]
except KeyError:
 print("the key you are trying to access does not exists")

print(chai_menu)

