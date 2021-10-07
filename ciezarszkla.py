while True:
    try:
        inp = input ("szerokosc [mm] = ")
        width = float(inp)
        inp = input ("wysokosc [mm] = ")
        height = float(inp)
        inp = input ("grubosc calkowita [mm] = ")
        thickness = float(inp)

        area = width*height/1000000
        weight = area*thickness*2.5
        print("pole powierzchni = ",round(area,2), " [m2]")
        print("ciezar to        = ", round(weight,2)," [kg]")
        print("****************************************************** \n")
    except:
        if inp == 'exit':
            break
        else:
            print("Nieprawidlowa Wartosc")
