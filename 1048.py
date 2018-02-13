salario = float(input())
if (salario >= 0 and salario <= 400.00):
    print ("Novo salario: %.2f" %((salario*0.15)+salario))
    print ("Reajuste ganho: %.2f" %(salario*0.15))
    print ("Em percentual: 15 %")
elif (salario >= 400.01 and salario <= 800.00):
    print ("Novo salario: %.2f" %((salario*0.12)+salario))
    print ("Reajuste ganho: %.2f" %(salario*0.12))
    print ("Em percentual: 12 %")
elif (salario >= 800.01 and salario <= 1200.00):
    print ("Novo salario: %.2f" %((salario*0.10)+salario))
    print ("Reajuste ganho: %.2f" %(salario*0.10))
    print ("Em percentual: 10 %")
elif (salario >= 1200.01 and salario <= 2000.00):
    print ("Novo salario: %.2f" %((salario*0.07)+salario))
    print ("Reajuste ganho: %.2f" %(salario*0.07))
    print ("Em percentual: 7 %")
elif (salario >= 2000.01):
    print ("Novo salario: %.2f" %((salario*0.04)+salario))
    print ("Reajuste ganho: %.2f" %(salario*0.04))
    print ("Em percentual: 4 %")
