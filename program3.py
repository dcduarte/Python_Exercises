my_orders = [["Amazon", "Earphones", 7.99, "10/03/18"], ["eBay", "Raspberry Pi 3", 28.79, "16/05/18"],
             ["eBuyer", "Hard Disk", 55.99, "22/04/18"], ["Gumtree", "Car", 500, "Collect in Person"]]

print(f"\nInformation on row 2 column 3: {my_orders[2][3]}")


print(f"\nGumtree Order information: {my_orders[3]}")

print("\nAll orders: ", *my_orders, sep="\n")

print(f"\nAll orders deleted confirmation: {my_orders.clear()}")
