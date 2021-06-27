class HExtras:
    def __init__(self):
        pass
    def calculoPago(self):
        ht, he, het= 0, 0, 0
        ph, phe, pt = 0, 0, 0
        ht = int(input("Ingrese horas trabajadas:"))
        ph = float(input("Ingrese valor por hora:"))
        if ht > 40:
            he = ht - 40
            if he > 8:
                het = he - 8
                he = 8
                phe = ph * 2 * he + ph * 3 * het
            else:
                phe = ph * 2 * he
            pt = ph * 40 + phe
        else:
            pt = ph * ht
        print("Horas extras: {} El pago de horas extras es de: {} El Salario total por horas trabajadas es de: {}".format(he,phe, pt))



HExtras = HExtras()
HExtras.calculoPago()