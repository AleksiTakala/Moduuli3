sukupuoli = input('Anna biologinen sukupuolesi ')
hemo = float(input('Anna hemoglobiini määräsi '))


if sukupuoli == "Mies":
    if hemo< 134:
        print("vähäinen määrä hemoglobiinia")
    elif hemo > 195:
        print("korkea määrä hemoglobiinia")
    else:
        print("Normaali määrä hemoglobiinia")



if sukupuoli == "Nainen":
    if hemo < 117:
        print("vähäinen määrä hemoglobiinia")
    elif hemo >175:
        print("korka määrä hemoglobiinia")
    else:
        print("Normaali määrä hemoglobiinia")