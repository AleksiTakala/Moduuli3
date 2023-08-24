vuosi = float(input('Anna vuosi '))

if (vuosi % 4 == 0):
    print("Vuosi on karkausvuosi")

elif(vuosi % 400 == 0) and (vuosi % 100 == 0):
    print("Vuosi on karkausvuosi")
else:
    print("Ei ole karkausvuosi")