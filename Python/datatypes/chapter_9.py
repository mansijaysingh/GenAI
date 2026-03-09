#Set
essential_spices={"cinnamon","cardamom","clove"}
optional_spices={"ginger","pepper","clove"}
all_spices=essential_spices|optional_spices
print(f"All spices:{all_spices}")

common_spices=essential_spices&optional_spices
print(f"Common spices:{common_spices}")

only_in_essential=essential_spices-optional_spices
print(f"Only in essential spices:{only_in_essential}")
