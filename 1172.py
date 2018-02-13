vetor = []
for i in range(10):
    entrada = int(input())
    if entrada<=0:
        vetor.append(1)
    else:
        vetor.append(entrada)
    print ("X[{}] = {}".format (i, vetor[i]))
    
