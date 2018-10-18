inventory = []
file = open("inventory.txt", "r")
for item in file:
  # print(item.strip())
  inventory.append(item.strip())
file.close()
print(inventory)