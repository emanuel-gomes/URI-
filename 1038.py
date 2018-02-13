l = input().split()
codigo = int(l[0])
quant = int(l[1])
if (codigo == 1):
    print ("Total: R$ %.2f" %(quant*4.00))
elif (codigo == 2):
    print ("Total: R$ %.2f" %(quant*4.50))
elif (codigo == 3):
    print ("Total: R$ %.2f" %(quant*5.00))
if (codigo == 4):
    print ("Total: R$ %.2f" %(quant*2.00))
if (codigo == 5):
    print ("Total: R$ %.2f" %(quant*1.50))
