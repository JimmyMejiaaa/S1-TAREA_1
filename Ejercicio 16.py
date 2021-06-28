class REPEAT:
    def __init__(self):
        pass
    def estCis6(self):
        i=1
        Serie=0
        nume= int(input("Ingrese un numero:"))
        band= True
        while band:
            if band ==True:
            Serie= Serie+(1/i)
            band= False
        else:
            Serie= Serie-(1/i)
            band= True
        i+=1
        if i > nume:
            break
        print("El resultado de la serie es: {}".format(Serie))