# SIMPLE INVENTORY SYSTEM - a dictionary-based system for adding, removing, searching, and updating electronic components.

e_components = {"resistor": 5, "capacitor": 2, "diode": 1} # components and their quantities

e_components["transistor"] = 11 # adding a new component to the inventory
del e_components["diode"] # removing a component from the inventory
print(e_components.get("transformer", 'Not found!')) # searching for a component in the inventory
e_components.update({"resistor": 20, "transistor": 8}) # updating the quantity of existing components in the inventory
print(e_components)
 