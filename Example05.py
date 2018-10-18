# file = open("inventory.txt", "a")
with open("inventory.txt", "a") as file:
  while True:
    newitem = input("Enter new inventory item: ")
    if newitem == "exit":
      print("All done!")
      break
    file.write(newitem + "\n")

