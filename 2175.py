L = input().split()
l1 = float(L[0])
l2 = float(L[1])
l3 = float(L[2])
if (l1 < l2 and l1 < l3):
	print("Otavio")
elif (l2 < l1 and l2<l3):
	print("Bruno")
elif (l3 < l1 and l3<l2):
	print("Ian")
else:
	print ("Empate")
