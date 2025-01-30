import moduleFONTOS

eredmeny = moduleFONTOS.ValaszBeolvas()


def PontokValasz(pont):
    if (pont >= 13 and pont <= 21):
        return eredmeny[0]
    elif (pont >= 22 and pont <= 30):
        return eredmeny[1]
    elif (pont >= 31 and pont <= 39):
        return eredmeny[2]