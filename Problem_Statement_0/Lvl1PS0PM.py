C = int(input())
N = int(input())
weights = []
for i in range(N):
  wi = int(input())
  weights.append(wi)
print("Total shipment weight: ", sum(weights))
print("Average container weight: ", avg(weights))
print("Heaviest Container: ", max(weights))
print("Lightest Container: ", min(weights))
print("Classification: ", end = "")
if sum(weights) >= 200:
  print("Heavy")
else:
  print("Light")
print("Port Capacity: ", C)
if sum(weights) <= C:
  print("Shipment can be unloaded.")
else:
  print("Shipment exceeds port capacity.")
