vet = []
cccore = int(input())
vet.append(cccore)
for i in range(1,10):
    vet.append(vet [len(vet)-1]*2)
for i in range(len(vet)):
    print ("N[%d] = %d" %(i,vet[i]))
