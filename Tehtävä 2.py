hytti = input('Anna hyttiluokkasi: ')

if hytti == "LUX":
    print("LUX hytti on parvekkeellinen hytti yläkannella.")
elif hytti == "A":
    print("A on ikkunallinen hytti autokanne yläpuolella")
elif hytti == "B":
    print("B on ikkunaton hytti autokanne yläpuolella")
elif hytti == "C":
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Tätä hytti luokkaa ei ole olemassa, laita kaikki kirjaimet isolla")