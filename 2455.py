l = input().split()
P1 = int(l[0])
C1 = int(l[1])
P2 = int(l[2])
C2 = int(l[3])
pe1 = P1*C1
pe2 = P2*C2
if (pe1==pe2):
    print("0")
elif (pe1>pe2):
    print("-1")
else:
    print("1")
