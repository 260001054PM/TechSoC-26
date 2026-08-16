Morship = "Y"
while Morship != "N":
  C = float(input())
  N = int(input())
  weights = []
  for i in range(N):
    wi = int(input())
    weights.append(wi)
  print("Total shipment weight: ", sum(weights))
  print("Average container weight: ", sum(weights)/len(weights))
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
  Morship = input("Do you want to process more ships? (Y/N): ")
print("Thank You")
