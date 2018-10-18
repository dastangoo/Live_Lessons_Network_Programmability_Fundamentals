inventory = []
# file = open("inventory.txt", "r")
with open("inventory.txt", "r") as file:
  for item in file:
    # print(item.strip())
    inventory.append(item.strip())
  # file.close()
print(inventory)