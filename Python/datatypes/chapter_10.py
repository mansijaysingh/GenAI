chai_order=dict(type="Ginger tea",size="Large", sugar=2)
print(f"chai order:{chai_order}")

chai_recipe={}
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="water and milk"
print(chai_recipe)
del chai_recipe["base"]
print(f"updated chai:{chai_recipe}")

print(f"is sugar in chai order?{'sugar' in chai_order}")

chai_order=dict(type="masala tea",size="medium", sugar=1)
print(f"chai order:{chai_order}")

last_item=chai_order.popitem()
print(f"last item removed:{last_item}")

extra_spices={"cardamom":1,"clove":2}
chai_recipe.update(extra_spices)
print(f"updated chai recipe:{chai_recipe}")