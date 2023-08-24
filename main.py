pituus = float(input('Anna kuhan pituus centtimetreinä '))


if (pituus < 37):
    alle = 37 - pituus
    print("Laske kuha takaisin veteen, kuha oli " , alle, " centtimetriä liian pieni")
else:
    print("Kuha on tarpeeksi iso")
