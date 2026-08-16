Morship = "Y"
def sorting(list):
  print("Sorted Way Of Weights: ")
  max = 0 #Since weight entered is positive
  sortedlist = []
  while list:
    for i in list:
      if i > max:
        max = i
    list.remove(max)
    sortedlist.append(max)
    max = 0
  for j in range(len(sortedlist)-1, -1, -1):
    print(sortedlist[j], end = " ")
while Morship != "N":
  C = float(input("Enter Maximum Storage Capacity: "))
  N = int(input("Enter the Number of Containers: "))
  weights = []
  for i in range(N):
    wi = int(input("Enter Weight: "))
    weights.append(wi)
  print("Total shipment weight: ", sum(weights))
  print("Average container weight: ", round(sum(weights)/len(weights), 2))
  print("Heaviest container: ", max(weights))
  print("Lightest container: ", min(weights))
  print("Classification: ", end = "")
  if sum(weights) >= 200:
    print("Heavy")
  else:
    print("Light")
  print("Port Capacity: ", C)
  print("Status: ", end = "")
  if sum(weights) <= C:
    print("Shipment can be unloaded")
  else:
    print("Shipment exceeds port capacity")
  sorting(weights)
  Morship = input("Do you want to process more ships? (Y/N): ")
print("Thank You")
